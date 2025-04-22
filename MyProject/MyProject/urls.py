from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('camera/<int:camera_id>/', views.camera_detail, name='camera_detail'),
    path('logout/', views.logout_view, name='logout'),
]
