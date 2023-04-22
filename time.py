import datetime
import time

while True:
    # Obtener la hora actual
    now = datetime.datetime.now()
    
    # Imprimir la hora actual en formato de reloj digital
    print(now.strftime("%H:%M:%S"), end="", flush=True)
    
    # Esperar un segundo antes de volver a imprimir la hora
    time.sleep(1)
    
    # Borrar la línea de la hora anterior
    print("\r", end="", flush=True)

