from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Libro
from .forms import CustomUserCreationForm, LibroForm, UserRegisterForm
from .forms import UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserChangeForm
from .models import Comentario


def inicio(request):
    return render(request, 'paginas/inicio.html')
def home(request):
    return render(request, 'paginas/home.html')
@login_required 
def nosotros(request):
    return render(request,'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})
def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario':formulario})

def editar(request,id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario' : formulario})
def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete() 
    return redirect('libros')

def register_view(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu cuenta ha sido creada correctamente! Por favor inicia sesión para acceder.')
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

@login_required
def editar_perfil(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('/')
    else:
        form = UserEditForm(initial={
            'username': user.username,
        })
    return render(request, 'editar_perfil.html', {'user_form': form})






def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

    context = {'form': form}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def comentarios(request):
    comentarios = Comentario.objects.all().order_by('-fecha')
    if request.method == 'POST':
        texto = request.POST.get('texto')
        comentario = Comentario(autor=request.user, texto=texto)
        comentario.save()
        return redirect('comentarios')
    return render(request, 'comentarios.html', {'comentarios': comentarios})

