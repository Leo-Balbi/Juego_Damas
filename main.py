import pygame
import sys
import random

ANCHO, ALTO = 600, 600
FILAS, COLUMNAS = 8, 8
TAM_CASILLA = ANCHO // COLUMNAS

BLANCO = (255, 255, 255)
GRIS = (160, 160, 160)
NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0)
VERDE = (0, 255, 0)

pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Damas")

# Tablero: 0 vacío, 1 jugador 1, 2 jugador 2, "D1" dama 1, "D2" dama 2
tablero = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]
for fila in range(FILAS):
    for col in range(COLUMNAS):
        if (fila + col) % 2 != 0:
            if fila < 3:
                tablero[fila][col] = 2
            elif fila > 4:
                tablero[fila][col] = 1

jugador = 1
seleccion = None
movimientos_posibles = []

def es_dama(f):
    return f == "D1" or f == "D2"

def dibujar_tablero():
    for fila in range(FILAS):
        for col in range(COLUMNAS):
            color = BLANCO if (fila + col) % 2 == 0 else GRIS
            pygame.draw.rect(ventana, color, (col * TAM_CASILLA, fila * TAM_CASILLA, TAM_CASILLA, TAM_CASILLA))
            ficha = tablero[fila][col]
            if ficha != 0:
                color_ficha = AMARILLO if ficha == 1 or ficha == "D1" else NEGRO
                pygame.draw.circle(ventana, color_ficha,
                                   (col * TAM_CASILLA + TAM_CASILLA // 2,
                                    fila * TAM_CASILLA + TAM_CASILLA // 2),
                                   TAM_CASILLA // 2 - 10)
                if es_dama(ficha):
                    pygame.draw.circle(ventana, BLANCO,
                        (col * TAM_CASILLA + TAM_CASILLA // 2,
                         fila * TAM_CASILLA + TAM_CASILLA // 2),
                        TAM_CASILLA // 4, 2)

    if seleccion:
        f, c = seleccion
        pygame.draw.rect(ventana, VERDE, (c * TAM_CASILLA, f * TAM_CASILLA, TAM_CASILLA, TAM_CASILLA), 3)
        for (f2, c2) in movimientos_posibles:
            pygame.draw.circle(ventana, VERDE,
                               (c2 * TAM_CASILLA + TAM_CASILLA // 2,
                                f2 * TAM_CASILLA + TAM_CASILLA // 2),
                               10)

def en_rango(f, c):
    return 0 <= f < FILAS and 0 <= c < COLUMNAS

def obtener_movimientos(f, c):
    ficha = tablero[f][c]
    if ficha == 0:
        return []

    movimientos = []
    direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    enemigo = [2, "D2"] if jugador == 1 else [1, "D1"]

    if es_dama(ficha):
        for df, dc in direcciones:
            i = 1
            while True:
                nf, nc = f + df*i, c + dc*i
                if not en_rango(nf, nc): break
                if tablero[nf][nc] == 0:
                    movimientos.append((nf, nc))
                    i += 1
                elif tablero[nf][nc] in enemigo:
                    salto_f, salto_c = nf + df, nc + dc
                    if en_rango(salto_f, salto_c) and tablero[salto_f][salto_c] == 0:
                        movimientos.append((salto_f, salto_c))
                    break
                else:
                    break
    else:
        avance = -1 if jugador == 2 else 1
        for dc in [-1, 1]:
            nf, nc = f + avance, c + dc
            if en_rango(nf, nc) and tablero[nf][nc] == 0:
                movimientos.append((nf, nc))
            elif en_rango(nf, nc) and tablero[nf][nc] in enemigo:
                salto_f, salto_c = nf + avance, nc + dc
                if en_rango(salto_f, salto_c) and tablero[salto_f][salto_c] == 0:
                    movimientos.append((salto_f, salto_c))
    return movimientos

def mover_ficha(f1, c1, f2, c2):
    global jugador
    ficha = tablero[f1][c1]
    tablero[f2][c2] = ficha
    tablero[f1][c1] = 0

    if abs(f2 - f1) == 2:
        mid_f = (f1 + f2) // 2
        mid_c = (c1 + c2) // 2
        tablero[mid_f][mid_c] = 0

    # Coronación
    if ficha == 1 and f2 == 0:
        tablero[f2][c2] = "D1"
    elif ficha == 2 and f2 == 7:
        tablero[f2][c2] = "D2"

    jugador = 2 if jugador == 1 else 1

def hay_ganador():
    j1 = any(cell in [1, "D1"] for row in tablero for cell in row)
    j2 = any(cell in [2, "D2"] for row in tablero for cell in row)
    if not j1:
        return 2
    if not j2:
        return 1
    return None

def mostrar_ganador(j):
    ventana.fill(NEGRO)
    fuente = pygame.font.SysFont("arial", 36, bold=True)
    texto = fuente.render(f"🎉 ¡Jugador {j} gana! 🎉", True, (255, 255, 0))
    ventana.blit(texto, (ANCHO//2 - texto.get_width()//2, ALTO//2 - texto.get_height()//2))
    pygame.display.flip()
    pygame.time.wait(4000)

# Bucle principal
reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            f, c = y // TAM_CASILLA, x // TAM_CASILLA
            if seleccion:
                if (f, c) in movimientos_posibles:
                    mover_ficha(seleccion[0], seleccion[1], f, c)
                    seleccion = None
                elif tablero[f][c] != 0 and ((jugador == 1 and tablero[f][c] in [1, "D1"]) or
                                             (jugador == 2 and tablero[f][c] in [2, "D2"])):
                    seleccion = (f, c)
                    movimientos_posibles = obtener_movimientos(f, c)
                else:
                    seleccion = None
            else:
                if tablero[f][c] != 0 and ((jugador == 1 and tablero[f][c] in [1, "D1"]) or
                                           (jugador == 2 and tablero[f][c] in [2, "D2"])):
                    seleccion = (f, c)
                    movimientos_posibles = obtener_movimientos(f, c)

    ventana.fill((0, 0, 0))
    dibujar_tablero()
    pygame.display.flip()

    ganador = hay_ganador()
    if ganador:
        mostrar_ganador(ganador)
        ejecutando = False

pygame.quit()
sys.exit()
