import pandas as pd
import random

# Lista de nombres de alumnos
alumnos = [
    "Juan Perez", "Maria Garcia", "Carlos Rodriguez", "Ana Martinez", 
    "Luis Hernandez", "Elena Lopez", "Pedro Sanchez", "Laura Gomez", 
    "Diego Diaz", "Sofia Torres"
]

# Lista de materias
materias = ["Matematicas", "Español", "Ciencias", "Historia", "Geografia"]

# Generar datos aleatorios de calificaciones (entre 4 y 10)
datos = []
for alumno in alumnos:
    fila = {"Alumno": alumno}
    for materia in materias:
        fila[materia] = random.randint(4, 10)
    datos.append(fila)

# Crear DataFrame y guardar en Excel
df = pd.DataFrame(datos)
df.to_excel("calificaciones_alumnos.xlsx", index=False)

print("Archivo 'calificaciones_alumnos.xlsx' generado con éxito.")
