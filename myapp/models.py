from django.db import models

# Create your models here.


class Movie(models.Model):
    name=models.CharField(max_length=200,unique=True)
    language=models.CharField(max_length=200)
    runtime=models.PositiveIntegerField()
    genre=models.CharField(max_length=200)
    director=models.CharField(max_length=200)
    actors=models.CharField(max_length=200)
    year=models.PositiveIntegerField()
    
    def __str__(self):
        return self.name

    
