#En el IDE de su preferencia realice un programa utilizando POO. (usar preferentemente Visual Studio Code).
#El programa debe crear un objeto ALUMNO, con propiedades tales como: nombre, edad, peso, promedio y metodos: inscripción, asesorias.
#Los metodos solo imprimiran un mensaje.
#Subir el programa a GitHub y compartir el link para acceder y poder calificar la actividad.

class alumno():
    nombre = "BetoCamacho"
    edad = 32
    peso = 202
    promedio = 4.5

    def inscripcion(self):
        print("El alumno se inscribio")

    def ascesorias(self):
        print("el alumno se asesoro")

miAlumno = alumno()

print("el alumno ",miAlumno.nombre," tiene ", miAlumno.edad," años")
miAlumno.inscripcion()
miAlumno.ascesorias()