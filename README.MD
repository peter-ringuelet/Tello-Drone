# Tello Drone Control

Este repositorio contiene un script de Python para controlar un dron Tello usando la biblioteca `djitellopy`. El script inicializa el dron, muestra y graba un video en tiempo real, y mueve el dron en un recorrido específico antes de regresarlo a la base.

## Requisitos

- Python 3.x
- djitellopy
- OpenCV

## Instalación

1. Clona el repositorio en tu máquina local:
    ```sh
    git clone https://github.com/peter-ringuelet/Tello-Drone.git
    cd Tello-Drone
    ```

2. Instala las dependencias necesarias:
    ```sh
    pip install djitellopy opencv-python
    ```

## Uso

1. Asegúrate de que tu dron Tello esté encendido y conectado a tu red WiFi.
2. Ejecuta el script:
    ```sh
    python tello_drone.py
    ```

## Funciones del Script

- `initialize_drone()`: Conecta el dron y activa la transmisión de video.
- `show_video(drone, out)`: Muestra el video en tiempo real del dron y lo graba en un archivo.
- `move_drone(drone)`: Mueve el dron en un recorrido específico y luego lo regresa a la base.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
