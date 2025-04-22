from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # Use Django's built-in User model for authentication
from app.models import Camera  # Ensure `Camera` model is defined in `models.py`

def signup_view(request):
    if request.method == 'POST':
        # Collect username and password from form
        username = request.POST['username']
        password = request.POST['password']

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        # Create new user
        User.objects.create_user(username=username, password=password)
        return redirect('login')  # Redirect to login page after successful signup

    return render(request, 'signup.html')  # Render signup form

def login_view(request):
    if request.method == 'POST':
        # Collect username and password from form
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)  # Log the user in
            return redirect('dashboard')  # Redirect to dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})  # Show error message

    return render(request, 'login.html')  # Render login form

@login_required
def dashboard(request):
    cameras = Camera.objects.all()
    return render(request, 'dashboard.html', {'user': request.user, 'cameras': cameras})

@login_required
def camera_detail(request, camera_id):
    camera = get_object_or_404(Camera, id=camera_id)
    return render(request, 'camera_detail.html', {'camera': camera})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
