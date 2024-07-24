from djitellopy import Tello
import time

# Inicializar el dron
drone = Tello()

try:
    # Conectar al dron
    drone.connect()
    print("Battery level:", drone.get_battery())
    
    # Esperar un momento para recibir paquetes de estado
    time.sleep(5)
    
    # Verificar si recibimos paquetes de estado
    if drone.get_height() is not None:
        print("Estado recibido correctamente.")
    else:
        print("No se recibió el estado del dron.")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Desconectar del dron
    drone.end()
