from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Camera(models.Model):
    CATEGORY_CHOICES = [
        ('dslr', 'DSLR'),
        ('mirrorless', 'Mirrorless'),
        ('point_and_shoot', 'Point & Shoot'),
        ('action', 'Action Cameras'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='dslr')
    sensor = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    video_capabilities = models.CharField(max_length=200)
    image_url = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CameraImage(models.Model):
    camera = models.ForeignKey(Camera, related_name='images', on_delete=models.CASCADE)
    url = models.URLField()
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.camera.name}"

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cameras = models.ManyToManyField(Camera)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wishlist for {self.user.username}" 