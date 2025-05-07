from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Camera, CameraImage, Wishlist
from django.db.models import Q

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

@login_required
def dashboard(request):
    search_query = request.GET.get('search', '')
    category = request.GET.get('category', '')

    cameras = Camera.objects.all()

    if search_query:
        cameras = cameras.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    if category and category != 'all':
        cameras = cameras.filter(category=category)

    return render(request, 'dashboard.html', {
        'cameras': cameras,
        'search_query': search_query,
        'selected_category': category
    })

@login_required
def camera_detail(request, camera_id):
    camera = get_object_or_404(Camera, id=camera_id)
    is_in_wishlist = False
    
    if hasattr(request.user, 'wishlist'):
        is_in_wishlist = camera in request.user.wishlist.cameras.all()
    
    return render(request, 'camera_detail.html', {
        'camera': camera,
        'is_in_wishlist': is_in_wishlist
    })

@login_required
def toggle_wishlist(request, camera_id):
    camera = get_object_or_404(Camera, id=camera_id)
    user = request.user

    if hasattr(user, 'wishlist'):
        if camera in user.wishlist.cameras.all():
            user.wishlist.cameras.remove(camera)
            is_in_wishlist = False
        else:
            user.wishlist.cameras.add(camera)
            is_in_wishlist = True
    else:
        wishlist = Wishlist.objects.create(user=user)
        wishlist.cameras.add(camera)
        is_in_wishlist = True

    return JsonResponse({
        'success': True,
        'is_in_wishlist': is_in_wishlist
    })

@login_required
def wishlist(request):
    if hasattr(request.user, 'wishlist'):
        cameras = request.user.wishlist.cameras.all()
    else:
        cameras = []
    
    return render(request, 'wishlist.html', {'cameras': cameras})

def logout_view(request):
    logout(request)
    return redirect('login') 