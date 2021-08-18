from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

class Cursos(models.Model):
    curso= models.TextField(verbose_name="Nombre del curso")
    duracion=models.TextField(max_length=12, verbose_name="Duracion del curso" )
    carrera=models.TextField()
    horario=models.CharField(max_length=10, verbose_name="Turno del curso")
    imagen=models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografia")
    nombre=models.TextField(verbose_name="Instructor")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name= "Curso"
        verbose_name_plural= "Cursos"
        ordering= ["created"]

    def __str__(self):
        return self.curso

class Comentario(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE,verbose_name="Curso")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado") 
    coment = RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]
    def __str__(self):
        return self.coment


class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    usuario = models.TextField(verbose_name="Usuario")
    correo = models.TextField(verbose_name="Email") 
    mensaje = models.TextField(verbose_name="Comentario") 
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado") 
    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]

    def __str__(self):
        return self.mensaje
        #Indica que se mostrára el mensaje como valor en la tabla

class ComentarioCurso(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    mate = models.TextField(verbose_name="Curso")
    turno = models.TextField(verbose_name="Turno")
    carrera = models.TextField(verbose_name="Carrera")
    instructor = models.TextField(verbose_name="Instructor")
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    class Meta:
        verbose_name = "Comentario Curso"
        verbose_name_plural = "Comentarios Cursos"
        ordering = ["-created"]
    def __str__(self):
        return self.carrera
    
class Archivos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    archivo = models.FileField(upload_to="archivos", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
        ordering = ["-created"]
    def __str__(self):
        return self.titulo