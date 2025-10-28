import sqlite3

class DatosTabla():

    conn = sqlite3.connect('DatosdelaTabla.db')
    c = conn.cursor()

    def crearTabla(self):
        self.c.execute ("""CREATE TABLE DatosdelaTabla(
                
                    User TEXT,
                    Pin INTEGER,
                    Name TEXT
                
        )""")
        self.conn.commit()

    def insertarTablas(self):

        self.c.execute("INSERT INTO DatosdelaTabla VALUES ('admin', '2705', 'Joseph')")

        Tdatos = [
            ('RObbert', 1234, 'Robbert'),
            ('Sararita', 2050, 'Sarah'),
            ('Stevenson', 2023, 'Steve')

        ]


        self.c.executemany("INSERT INTO DatosdelaTabla VALUES (?, ?, ?)", Tdatos)
        self.conn.commit()

    def Eliminardato(self):
        print("El super usuario no puede ser eliminado")
        print("El super usuario es: admin con pin 2705")
        print("desea eliminar un elemento de la tabla?")
        respuesta = input("si o no: ")
        if respuesta == 'si':
            print("para continuar escriba su nombre de usuario y su pin: ")
            user = input("Usuario: ")
            pin = int(input("Pin: "))
            if user == 'admin' and pin == 2705:
                print("Que usuario desea eliminar: ")
                userdelete = input("Usuario a eliminar: ")
                if userdelete == 'admin':
                    print("El super usuario no puede ser eliminado")
                    print("continuemos con la demostracion")
                else:
                    self.c.execute("DELETE FROM DatosdelaTabla WHERE User = ?", (userdelete,))
                    self.conn.commit()
            else:
                print("no tiene permisos para eliminar usuarios o sus credenciales son incorrectas verifique nuevamente") 
                print("continuemos con la demostracion")
        
            print("Usuario eliminado")
        else:
            print("continuemos con la demostracion")
        
        
    def modificarElemento(self):
        print("desea modificar un elemento de la tabla?")
        respuesta = input("si o no: ")
        if respuesta == 'si':
            print("Escriba su usuario y su Pin: ")
            user = input("Usuario: ")
            pin = int(input("Pin: "))
            if user == 'admin' and pin == 2705:
                print("Escriba el nombre de usuario y el pin que desea modificar: ")
                usermodify = input("Usuario a modificar: ")
                pinmodify = int(input("Pin a modificar: "))
                if usermodify == 'admin' and pinmodify == 2705:
                    print("El super usuario no puede ser modificado")
                    print("continuemos con la demostracion")
                    
                else:
                    print("Escriba el nuevo nombre de usuario y pin que desea modificar: ")
                    newuser = input("Nuevo usuario: ")
                    newpin = int(input("Nuevo pin: "))
                    self.c.execute("UPDATE DatosdelaTabla SET User = ?, Pin = ? WHERE User = ? AND Pin = ?", (newuser, newpin, usermodify, pinmodify))
                    self.conn.commit()
                    print("Elemento modificado")
            else:
                print("no tiene permisos para modificar usuarios o sus credenciales son incorrectas verifique nuevamente")
        else:
            print("seria todo")
            exit(0)
            print("el nombre no puede ser modificado")

    def actualizarTabla(self):
        self.c.execute("DROP TABLE IF EXISTS DatosdelaTabla")
        self.crearTabla()
        self.insertarTablas()

misDatos = DatosTabla()

misDatos.actualizarTabla()
#misDatos.crearTabla()
misDatos.insertarTablas()
misDatos.actualizarTabla()
misDatos.Eliminardato()
misDatos.modificarElemento()