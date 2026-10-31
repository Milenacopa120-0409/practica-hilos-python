# Práctica: Sistema de Archivos Concurrente

**Integrantes:** Copa, Perez, Bustamante, Milena

## Descripción
Este programa simula un sistema de clasificación de 24 documentos utilizando concurrencia en Python. 
- Se utilizan 4 hilos (trabajadores) concurrentes.
- Se emplea una cola compartida (`queue.Queue`) para distribuir los trabajos.
- Se utiliza un candado (`threading.Lock`) para proteger la actualización del diccionario de resultados compartido y evitar condiciones de carrera.
- Se utiliza `get_nowait()` para que los hilos terminen de forma controlada cuando la cola esté vacía.

## Ejecución
Para ejecutar el programa, abre la terminal y escribe:
`python practica.py`
