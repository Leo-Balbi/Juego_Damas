import pygame
import sys
import random

# Constantes
ANCHO, ALTO = 600, 600
FILAS, COLUMNAS = 8, 8
TAM_CASILLA = ANCHO // COLUMNAS

# Colores actualizados
BLANCO = (255, 255, 255)
GRIS_CLARO = (200, 200, 200)
NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0)
VERDE = (0, 255, 0)

# Inicializar Pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Damas")

# Tablero y fichas
tablero = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]
for fila in range(FILAS):
    for col in range(COLUMNAS):
        if (fila + col) % 2 != 0:
            if fila < 3:
                tablero[fila][col] = 1  # Jugador 1 (amarillo)
            elif fila > 4:
                tablero[fila][col] = 2  # Jugador 2 (negro)

# Ficha seleccionada y jugador actual
sel_fila, sel_col = 0, 1
jugador = 1
movimiento_multiple = False  # Para capturas múltiples

def dibujar_ficha_3d(ventana, color_base, x, y, radio):
    # Círculo base
    pygame.draw.circle(ventana, color_base, (x, y), radio)
    # Círculo de luz (más claro) para simular volumen
    color_luz = tuple(min(255, c + 60) for c in color_base)
    pygame.draw.circle(ventana, color_luz, (x - radio // 3, y - radio // 3), radio // 2)

def dibujar_tablero():
    for fila in range(FILAS):
        for col in range(COLUMNAS):
            color = BLANCO if (fila + col) % 2 == 0 else GRIS_CLARO
            pygame.draw.rect(ventana, color, (col * TAM_CASILLA, fila * TAM_CASILLA, TAM_CASILLA, TAM_CASILLA))

            ficha = tablero[fila][col]
            if ficha != 0:
                color_ficha = AMARILLO if ficha == 1 or ficha == "D1" else (NEGRO if ficha == 2 or ficha == "D2" else BLANCO)
                x = col * TAM_CASILLA + TAM_CASILLA // 2
                y = fila * TAM_CASILLA + TAM_CASILLA // 2
                radio = TAM_CASILLA // 2 - 10
                dibujar_ficha_3d(ventana, color_ficha, x, y, radio)
                # Opcional: Dibujar símbolo de dama (por ejemplo, un círculo pequeño)
                if ficha == "D1" or ficha == "D2":
                    pygame.draw.circle(ventana, (255, 255, 255), (x, y), TAM_CASILLA // 6)

    # Dibujar cursor
    pygame.draw.rect(ventana, VERDE, (sel_col * TAM_CASILLA, sel_fila * TAM_CASILLA, TAM_CASILLA, TAM_CASILLA), 3)

def es_dama(ficha):
    return ficha == "D1" or ficha == "D2"

def mover_ficha(d_fila, d_col):
    global sel_fila, sel_col, jugador, movimiento_multiple

    ficha_sel = tablero[sel_fila][sel_col]
    if ficha_sel == 0 or (ficha_sel != jugador and ficha_sel != f"D{jugador}"):
        return

    # Dama: movimiento libre en diagonal
    if es_dama(ficha_sel):
        pasos = 1
        while True:
            nueva_fila = sel_fila + pasos * d_fila
            nueva_col = sel_col + pasos * d_col
            if 0 <= nueva_fila < FILAS and 0 <= nueva_col < COLUMNAS:
                if tablero[nueva_fila][nueva_col] == 0:
                    # Movimiento libre
                    ult_fila, ult_col = nueva_fila, nueva_col
                    pasos += 1
                else:
                    break
            else:
                break
        # Si hay al menos un movimiento posible
        if pasos > 1:
            tablero[ult_fila][ult_col] = ficha_sel
            tablero[sel_fila][sel_col] = 0
            sel_fila, sel_col = ult_fila, ult_col
            # No coronación, ya es dama
            jugador = 2 if jugador == 1 else 1
            movimiento_multiple = False
            return

        # Captura múltiple de dama
        pasos = 1
        while True:
            mid_fila = sel_fila + pasos * d_fila
            mid_col = sel_col + pasos * d_col
            next_fila = sel_fila + (pasos + 1) * d_fila
            next_col = sel_col + (pasos + 1) * d_col
            if (0 <= mid_fila < FILAS and 0 <= mid_col < COLUMNAS and
                0 <= next_fila < FILAS and 0 <= next_col < COLUMNAS):
                mid_ficha = tablero[mid_fila][mid_col]
                if mid_ficha != 0 and mid_ficha != ficha_sel and tablero[next_fila][next_col] == 0:
                    # Comer
                    tablero[next_fila][next_col] = ficha_sel
                    tablero[sel_fila][sel_col] = 0
                    tablero[mid_fila][mid_col] = 0
                    sel_fila, sel_col = next_fila, next_col
                    # Ver si puede seguir comiendo
                    if puede_comer(sel_fila, sel_col, ficha_sel):
                        movimiento_multiple = True
                    else:
                        jugador = 2 if jugador == 1 else 1
                        movimiento_multiple = False
                    return
                elif mid_ficha == 0:
                    pasos += 1
                else:
                    break
            else:
                break

    # Pieza normal (no dama)
    else:
        nueva_fila = sel_fila + d_fila
        nueva_col = sel_col + d_col
        if 0 <= nueva_fila < FILAS and 0 <= nueva_col < COLUMNAS:
            if tablero[nueva_fila][nueva_col] == 0:
                # Movimiento normal (solo hacia adelante)
                if (jugador == 1 and d_fila == 1) or (jugador == 2 and d_fila == -1):
                    tablero[nueva_fila][nueva_col] = ficha_sel
                    tablero[sel_fila][sel_col] = 0
                    # Coronación
                    if jugador == 1 and nueva_fila == 7:
                        tablero[nueva_fila][nueva_col] = "D1"
                    elif jugador == 2 and nueva_fila == 0:
                        tablero[nueva_fila][nueva_col] = "D2"
                    sel_fila, sel_col = nueva_fila, nueva_col
                    jugador = 2 if jugador == 1 else 1
                    movimiento_multiple = False
            # Comer
            elif (0 <= sel_fila + 2 * d_fila < FILAS and
                  0 <= sel_col + 2 * d_col < COLUMNAS and
                  tablero[nueva_fila][nueva_col] != 0 and
                  tablero[nueva_fila][nueva_col] != ficha_sel and
                  tablero[sel_fila + 2 * d_fila][sel_col + 2 * d_col] == 0):
                tablero[sel_fila + 2 * d_fila][sel_col + 2 * d_col] = ficha_sel
                tablero[sel_fila][sel_col] = 0
                tablero[nueva_fila][nueva_col] = 0
                nueva_fila = sel_fila + 2 * d_fila
                nueva_col = sel_col + 2 * d_col
                # Coronación después de comer
                if jugador == 1 and nueva_fila == 7:
                    tablero[nueva_fila][nueva_col] = "D1"
                elif jugador == 2 and nueva_fila == 0:
                    tablero[nueva_fila][nueva_col] = "D2"
                sel_fila, sel_col = nueva_fila, nueva_col
                # Ver si puede seguir comiendo
                if puede_comer(sel_fila, sel_col, tablero[sel_fila][sel_col]):
                    movimiento_multiple = True
                else:
                    jugador = 2 if jugador == 1 else 1
                    movimiento_multiple = False

def puede_comer(fila, col, ficha_sel):
    direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for d_fila, d_col in direcciones:
        # Dama: puede saltar varias veces
        if es_dama(ficha_sel):
            pasos = 1
            while True:
                mid_fila = fila + pasos * d_fila
                mid_col = col + pasos * d_col
                next_fila = fila + (pasos + 1) * d_fila
                next_col = col + (pasos + 1) * d_col
                if (0 <= mid_fila < FILAS and 0 <= mid_col < COLUMNAS and
                    0 <= next_fila < FILAS and 0 <= next_col < COLUMNAS):
                    mid_ficha = tablero[mid_fila][mid_col]
                    if mid_ficha != 0 and mid_ficha != ficha_sel and tablero[next_fila][next_col] == 0:
                        return True
                    elif mid_ficha == 0:
                        pasos += 1
                    else:
                        break
                else:
                    break
        else:
            mid_fila = fila + d_fila
            mid_col = col + d_col
            next_fila = fila + 2 * d_fila
            next_col = col + 2 * d_col
            if (0 <= mid_fila < FILAS and 0 <= mid_col < COLUMNAS and
                0 <= next_fila < FILAS and 0 <= next_col < COLUMNAS):
                mid_ficha = tablero[mid_fila][mid_col]
                if mid_ficha != 0 and mid_ficha != ficha_sel and tablero[next_fila][next_col] == 0:
                    return True
    return False

def hay_ganador():
    jugador1_vive = any(1 in fila or "D1" in fila for fila in tablero)
    jugador2_vive = any(2 in fila or "D2" in fila for fila in tablero)
    if not jugador1_vive:
        return 2
    if not jugador2_vive:
        return 1
    return None

def mostrar_ganador(jugador):
    ventana.fill((0, 0, 0))  # Fondo negro
    fuente = pygame.font.SysFont("arial", 40, bold=True)

    mensaje = f"🎆🎉 ¡Jugador {jugador} ha ganado! 🎉🎆"
    texto = fuente.render(mensaje, True, (255, 215, 0))  # Dorado
    ventana.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))

    # Simulación de fuegos artificiales con círculos de colores
    for _ in range(50):
        x = random.randint(50, ANCHO - 50)
        y = random.randint(50, ALTO - 50)
        radio = random.randint(5, 20)
        color = random.choice([(255, 0, 0), (0, 255, 0), (0, 150, 255), (255, 255, 0)])
        pygame.draw.circle(ventana, color, (x, y), radio)

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

        if evento.type == pygame.KEYDOWN:
            # Controles con teclado numérico (sin Num Lock)
            if evento.key == pygame.K_KP7:  # Arriba izquierda
                mover_ficha(-1, -1)
            elif evento.key == pygame.K_KP9:  # Arriba derecha
                mover_ficha(-1, 1)
            elif evento.key == pygame.K_KP1:  # Abajo izquierda
                mover_ficha(1, -1)
            elif evento.key == pygame.K_KP3:  # Abajo derecha
                mover_ficha(1, 1)

    ganador = hay_ganador()
    if ganador is not None:
        mostrar_ganador(ganador)
        ejecutando = False

    dibujar_tablero()
    pygame.display.flip()

pygame.quit()
sys.exit()
