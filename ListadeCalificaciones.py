class ListadeCalificaciones():
    calificaciones=[]
    nombres=[]
    promedio=0.00
    nombresmayor=[]
    def leer(self):
        for i in range(3):
            #leer en una lista las calificaciones de 10 alumnos y sus nombres.
            self.calificaciones.append (int(input("ingrese la calificacion" + str(i+1) + ": ")))
            self.nombres.append (input(f"ingrese el nombre del alumno {i+1}: "))
        

    def proceso(self):
        print(self.calificaciones)
        #obtener el promedio grupal de calificación
        promedio = sum(ListadeCalificaciones().calificaciones) / len(ListadeCalificaciones().calificaciones)
        #lista de los alumnos con promedio mayor a 9.5
        self.nombresmayor.append([self.nombres[i] for i in range(len(ListadeCalificaciones().calificaciones)) if ListadeCalificaciones().calificaciones[i] > 9.5])

    def imprimir(self):
        #imprimir los resultados.
        print(f"el promedio grupal es: {sum(ListadeCalificaciones().calificaciones) / len(ListadeCalificaciones().calificaciones)}")
        print(f"el nombre de los alumnos con promedio mayor a 9.5 es: {ListadeCalificaciones().nombresmayor}")



ListadeCalificaciones().leer()
ListadeCalificaciones().proceso()
ListadeCalificaciones().imprimir()
