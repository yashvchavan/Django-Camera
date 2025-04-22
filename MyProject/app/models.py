from django.db import models

class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class Camera(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='camera_images/')
    details = models.TextField()

    def __str__(self):
        return self.name
