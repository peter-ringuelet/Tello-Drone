from djitellopy import Tello
import cv2
from threading import Thread
import time


# Inicializar el dron
def initialize_drone():
    drone = Tello()
    drone.connect()
    print(f"Battery level: {drone.get_battery()}%")
    drone.streamon()
    return drone


# Función para mostrar y grabar el video en tiempo real
def show_video(drone, out):
    frame_read = drone.get_frame_read()
    while True:
        img = frame_read.frame
        out.write(img)  # Grabar el frame en el archivo de video
        cv2.imshow("Tello Video Stream", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()
    drone.streamoff()
    drone.end()


# Función para mover el dron y regresar a la base con velocidad máxima
def move_drone(drone):
    # Despegar el dron
    drone.takeoff()

    # Subir a 1 metro de altura (100 cm)
    drone.move_up(100)

    # Configurar la velocidad máxima
    max_speed = 100  # La velocidad máxima en cm/s
    drone.set_speed(max_speed)

    # Avanzar 720 cm
    drone.move_forward(500)  # Primer tramo de 5 metros
    drone.move_forward(220)  # Segundo tramo de 2.2 metros

    # Girar 90 grados a la derecha
    drone.rotate_clockwise(90)

    # Avanzar 280 cm
    drone.move_forward(260)

    # Realizar el recorrido adicional
    # Girar 90 grados a la izquierda
    drone.rotate_counter_clockwise(90)

    # Avanzar 200 cm
    drone.move_forward(200)

    # Regresar a la posición inicial
    drone.rotate_clockwise(180)  # Girar 180 grados
    drone.move_forward(200)  # Regresar 200 cm
    drone.rotate_clockwise(90)  # Girar 90 grados a la derecha
    drone.move_forward(260)  # Regresar 280 cm
    drone.rotate_counter_clockwise(90)  # Girar 90 grados a la izquierda
    drone.move_forward(220)  # Regresar 220 cm
    drone.move_forward(500)  # Regresar 500 cm

    # Bajar a la altura inicial
    drone.move_down(100)

    # Aterrizar el dron
    drone.land()


if __name__ == "__main__":
    # Inicializar el dron
    drone = initialize_drone()

    # Configurar grabación de video
    frame_read = drone.get_frame_read()
    height, width, _ = frame_read.frame.shape
    out = cv2.VideoWriter('tello_video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    # Iniciar el hilo de video en paralelo
    video_thread = Thread(target=show_video, args=(drone, out))
    video_thread.start()

    # Mover el dron y regresar a la base con velocidad máxima
    move_drone(drone)

    video_thread.join()

