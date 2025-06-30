# 🎲 Juego de Damas - Proyecto en Python con Pygame 🎲

---

![Banner](https://img.shields.io/badge/Juego%20de%20Damas-Pygame-blueviolet?style=for-the-badge&logo=python)

---

## 🎯 Descripción

¡Bienvenido al **Juego de Damas**!  
Un clásico juego de estrategia implementado en Python usando la librería **Pygame**, donde dos jugadores se enfrentan en un tablero de 8x8 para capturar las fichas del oponente y coronar sus piezas para obtener ventaja.

Este proyecto incluye:

- Tablero visual atractivo con colores claros y modernos.
- Fichas con efecto 3D para una experiencia visual mejorada.
- Reglas clásicas y avanzadas de damas, incluyendo movimientos ilimitados para damas coronadas y capturas múltiples.
- Mensajes de fin de juego con animaciones de fuegos artificiales.

---

## 🚀 Instalación

Sigue estos pasos para instalar y ejecutar el juego en tu equipo:

### Requisitos previos

- Python 3.7 o superior (recomendado Python 3.13.3)
- Pygame 2.6.1 o superior

### Pasos


1. **Crea un entorno virtual (opcional pero recomendado):**

python -m venv venv

2. **Instala las dependencias:**

pip install pygame


3. **Ejecuta el juego:**

python main.py


---

## 🎮 Instrucciones del Juego

- El juego es para **2 jugadores** que alternan turnos.
- Cada jugador controla un conjunto de fichas:
  - **Jugador 1:** Fichas amarillas
  - **Jugador 2:** Fichas negras
- El tablero es de 8x8 casillas, con casillas blancas y gris claro alternadas.
- El cursor verde indica la ficha seleccionada.

### Controles

Usa el teclado numérico para mover la ficha seleccionada:

| Tecla | Movimiento          |
|-------|---------------------|
| 7     | Arriba izquierda    |
| 9     | Arriba derecha      |
| 1     | Abajo izquierda     |
| 3     | Abajo derecha       |

### Movimiento de fichas

- Las fichas normales se mueven una casilla en diagonal hacia adelante.
- Cuando una ficha alcanza la fila de fondo del oponente, se corona y se convierte en **Dama**.
- Las **Damas** pueden moverse cualquier cantidad de casillas en diagonal, hacia cualquier dirección.
- Se pueden realizar capturas saltando sobre fichas enemigas:
  - Las capturas pueden ser múltiples en un solo turno si hay más fichas para comer.
  - Después de una captura, si es posible seguir capturando, el jugador debe continuar.

---

## 🏁 Reglas del Juego

1. **Objetivo:** Capturar todas las fichas del oponente o dejarlo sin movimientos posibles.
2. **Captura obligatoria:** Si una captura es posible, el jugador debe realizarla.
3. **Coronación:** Al llegar a la última fila del oponente, la ficha se corona y gana movimientos ilimitados en diagonal.
4. **Turnos alternos:** Los jugadores se turnan para mover una ficha válida.
5. **Fin del juego:** El juego termina cuando un jugador pierde todas sus fichas o no puede mover.

---

## 🎨 Detalles Visuales

- **Tablero:** Casillas blancas y gris claro para facilitar la visualización.
- **Fichas:**  
  - Amarillas para el Jugador 1  
  - Negras para el Jugador 2  
  - Efecto 3D con sombras y luces para mayor realismo.
- **Damas:** Identificadas con un círculo blanco pequeño en el centro.
- **Cursor:** Cuadro verde que indica la ficha seleccionada para mover.
- **Animaciones:** Mensajes de victoria con fuegos artificiales coloridos.

---

## 📂 Estructura del Proyecto

Juego_Damas/
│
├── main.py # Código principal del juego
├── README.md # Este archivo
├── requirements.txt # (opcional) Dependencias del proyecto
└── assets/ # (opcional) Recursos gráficos y sonidos


---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!  
Si quieres mejorar el juego, reportar errores o sugerir nuevas funcionalidades, por favor abre un issue o un pull request en GitHub.

---

## 📞 Contacto

Desarrollado por **Leonardo Balbi**  
Correo: leonardobalbi22112@gmail.com  
GitHub: [Leo-Balbi](https://github.com/Leo-Balbi)

---

## 🎉 ¡Diviértete jugando y aprendiendo a programar con este proyecto clásico!



