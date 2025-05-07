from django.contrib import admin
from app.models import Camera, CameraImage

@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(CameraImage)
class CameraImageAdmin(admin.ModelAdmin):
    list_display = ('camera', 'is_primary')
    list_filter = ('is_primary',)
