import sqlite3

class TablasAlumnos():

    conn = sqlite3.connect('alumnosConalep.db')
    c = conn.cursor()

    def crearTabla(self):
        self.c.execute ("""CREATE TABLE alumnosConalep(
                
                    nombre TEXT,
                    edad INTEGER,
                    matricula INTEGER
                
        )""")
        self.conn.commit()

    def insertarTablas(self):

        self.c.execute("INSERT INTO alumnosConalep VALUES ('Joseph', 17, 231690507-0)")

        Testudiantes = [

            ('Yuren', 16, 231690804-0),
            ('Beto', 17, 231690912-0),
            ('Hugo', 16, 231690203-0)

        ]

        self.c.executemany("INSERT INTO alumnosConalep VALUES (?, ?, ?)", Testudiantes)

        self.conn.commit()
        


    def imprimirDatos(self):

        self.c.execute("SELECT * FROM alumnosConalep")
        x = (self.c.fetchall())

        for i in x:
            print(i)
        self.conn.commit()
        self.conn.close()

        



miBase = TablasAlumnos()

miBase.crearTabla()
miBase.insertarTablas()
miBase.imprimirDatos()
