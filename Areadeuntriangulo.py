class tri():
    base = 0.00
    altura = 0.00 
    area = 0.00

    def Leer(self):
        tri.base = float(input("cual es la base del triangulo: "))
        tri.altura = float(input("cual es la altura del triangulo: "))

    def calcular(self):
        tri.area = tri.base * tri.altura / 2

    def imprimir(self):
        print("la base del triangulo es: ", tri.base)
        print("la altura del triangulo es: ", tri.altura)
        print("el area del triangulo es: ", tri.area)


ATriangulo = tri()
ATriangulo.Leer()
ATriangulo.calcular()
ATriangulo.imprimir()