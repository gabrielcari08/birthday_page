from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Card


def welcome_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    login_error = None
    register_error = None
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                login_error = "Usuario o contraseña incorrectos"
        
        elif action == 'register':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password_confirm = request.POST.get('password_confirm')
            
            if User.objects.filter(username=username).exists():
                register_error = "El usuario ya existe"
            elif password != password_confirm:
                register_error = "Las contraseñas no coinciden"
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                return redirect('home')
    
    return render(request, 'welcome.html', {
        'login_error': login_error,
        'register_error': register_error
    })


@login_required(login_url='/')
def home_view(request):
    cards = Card.objects.all().order_by('created_at')
    return render(request, 'home.html', {'cards': cards})


def logout_view(request):
    logout(request)
    return redirect('/')
