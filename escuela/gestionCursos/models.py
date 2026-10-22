from django.db import models

# Create your models here.
#CREACION DE MODELOS A TRABAJAR 
#Creacion de funciones para reutilizar en los argumentos 
def pais():
    paises = [
        ("BRA","Brasil"),
        ("COL", "Colombia"),
        ("CAN", "Canadá"),
        ("CHN", "China"),
        ("ECU", "Ecuador"),
        ("ESP", "España"),
        ("USA", "Estados Unidos"),
        ("PER", "Perú"),
        ("PRI", "Puerto Rico"),
        ("GBR", "Reino Unido"),
        ("SLV", "Salvador") ]

    return paises
def idioma():

    idiomas = [
        ("de","Alemán"),
        ("es","Español"),
        ("fr","Frances"),
        ("en","Inglés"),
        ("zh","Mandarín"),
        ("pt","Portugues")]

    return idiomas
def genero():
    generos = [
        ("MOD", "Modelado y arte 3D"),
        ("PRO", "Programación"),
        ("ANI", "Animación y Rigging")
    ]

    return generos
def curso():
    cursos = [
        ("CH", "C#"), #Pares y valores de etiquetas
        ("JS", "JavaScript"),
        ("CP", "C++"),
        ("PY", "Python"),
        ("BL", "Blender")
    ]

    return cursos
#CREACION DE MODELO PROFESOR Y SUS ATRIBUTOS
class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=55)
    apellido_profesor = models.CharField(max_length=55, blank=True, null=True)
    email_profesor = models.EmailField(max_length=50)
    edad_profesor = models.DateField()
    pais_profesor = models.CharField(max_length=20, choices=pais())
    idioma_profesor = models.CharField(max_length=20, choices=idioma())

#CREACION DE MODELO ESTUDIANTE Y SUS ATRIBUTOS
class Estudiante(models.Model):
    nombre_estudiante = models.CharField(max_length=55)
    apellido_estudiante = models.CharField(max_length=55, blank=True, null=True)
    email_estudiante = models.EmailField(max_length=50)
    edad_estudiante = models.DateField()
    pais_estudiante = models.CharField(max_length=20, choices=pais())
    idioma_estudiante = models.CharField(max_length=20, choices=idioma())

#CREACION DE MODELO CURSO Y SUS ATRIBUTOS
class Curso(models.Model):
    nombre_curso = models.CharField(max_length=55, choices=curso())
    genero_curso = models.CharField(max_length=50, choices= genero())
    precio_curso = models.FloatField()
    descripcion_curso = models.TextField()
    estado = models.BooleanField()
    id_profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT)

#CREACION DE MODELO CURSO_ESTUDINATE Y SUS ATRIBUTOS PARA EVITAR EL MUCHO A MUCHOS
class Curso_Estudiante(models.Model):
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)