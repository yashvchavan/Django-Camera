from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('camera/<int:camera_id>/', views.camera_detail, name='camera_detail'),
    path('compare/<str:camera_ids>/', views.compare_cameras, name='compare_cameras'),
    path('wishlist/toggle/<int:camera_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
