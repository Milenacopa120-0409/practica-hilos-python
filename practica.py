import threading
import queue
import time
import random

# --- Configuración inicial ---
trabajos = queue.Queue()
resultados = {}
lock = threading.Lock()

# Cargar 24 documentos en la cola
for doc_id in range(1, 25):
    # Tamaño simulado entre 1 y 5 (según lo visto en clase)
    tamano_simulado = random.randint(1, 5) 
    trabajos.put((doc_id, tamano_simulado))

# --- TODO 1 y 2 y 3 y 4: Función del trabajador ---
def trabajador(nombre):
    contador_local = 0
    
    while True:
        try:
            # Retirar trabajo de la cola sin bloquear (get_nowait)
            doc_id, tamano = trabajos.get_nowait()
            
            # Simular el procesamiento (tamaño * 0.1)
            time.sleep(tamano * 0.1)
            
            # Contar el documento procesado localmente
            contador_local += 1
            
            # Actualizar resultados dentro del lock (Sincronización)
            with lock:
                resultados[nombre] = contador_local
                
            # Indicar que la tarea se completó
            trabajos.task_done()
            
        except queue.Empty:
            # Si la cola está vacía, el hilo termina de forma controlada
            break

# --- TODO 5: Iniciar hilos y esperar con join() ---
nombres_trabajadores = ["Copa", "Perez", "Bustamante", "Milena"]
hilos = []

print("Iniciando el procesamiento de 24 documentos...\n")

for nombre in nombres_trabajadores:
    # Crear el hilo apuntando a la función y pasando el nombre
    hilo = threading.Thread(target=trabajador, args=(nombre,))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

# --- TODO 6: Mostrar total y resumen por trabajador ---
print("\n" + "="*40)
print("       RESUMEN DE EJECUCIÓN")
print("="*40)

# Calcular total procesado
total_procesado = sum(resultados.values())

# Mostrar resumen individual
for nombre, cantidad in resultados.items():
    print(f"Trabajador {nombre:10} : procesó {cantidad} documentos.")

print("-" * 40)
print(f"TOTAL DE DOCUMENTOS PROCESADOS: {total_procesado}")
print("="*40)
print("Todas las tareas terminaron correctamente.")
