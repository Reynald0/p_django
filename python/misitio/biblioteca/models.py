from django.db import models

class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    website = models.URLField()

    class META: # Esta clase interna de Editor es de utilidad ya que muestra el nombre de 'Autores' en la interfaz de administracion, 'orderin = ' permite ordenar de una vez una busqueda por nombre.
        ordering = ['nombre'] 
        verbose_name_plural = "Editores"


    def __str__(self): # __unicode__ en python2
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)
    email = models.URLField()

    class META: # Esta clase interna de Autor es de utilidad ya que muestra el nombre de 'Autores' en la interfaz de administracion.
        ordering = ['nombre'] 
        verbose_name_plural = "Autores"

    def __str__(self):
        return "%s %s" %(self.nombre, self.apellidos)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to = 'portadas')

    #class META: # Esta clase interna de Libro es de utilidad ya que muestra el nombre de 'Libros' en la interfaz de administracion, pero no es realmente necesario ya que por defecto la interfaz le agrega una 's'.
    #    verbose_name_plural = "Libros"

    def __str__(self):
        return self.titulo


