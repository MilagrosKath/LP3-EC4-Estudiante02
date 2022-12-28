from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    idcourse = models.CharField(max_length=30, default=0)
    contenido = models.CharField(max_length=100)
    image = models.ImageField(default='null')
    state = models.CharField(max_length=20)

    