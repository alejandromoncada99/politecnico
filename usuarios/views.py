from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import rol_requerido
from .models import Curso
from .models import CarouselSlide

def home(request):
    return render(request, 'usuarios/home.html')

def sobre_nosotros(request):
    return render(request, 'usuarios/sobre_nosotros.html')


def cursos(request):
    return render(request, 'usuarios/cursos.html')


def contacto(request):
    return render(request, 'usuarios/contacto.html')


def login(request):
    return render(request, 'usuarios/login.html')


# ----------------------
# Dashboards
# ----------------------
@login_required
@rol_requerido(['docente'])
def crear_curso(request):
    cursos = Curso.objects.filter(docente=request.user)
    return render(request, 'usuarios/docente_dashboard.html', {'cursos': cursos})


@login_required
@rol_requerido(['estudiante'])
def cursos_disponibles(request):
    cursos = Curso.objects.filter(activo=True)
    return render(request, 'usuarios/estudiante_dashboard.html', {'cursos': cursos})

# ----------------------
# Redirección por rol
# ----------------------
@login_required
def redireccion_por_rol(request):
    if request.user.groups.filter(name='docente').exists():
        return redirect('crear_curso')
    if request.user.groups.filter(name='estudiante').exists():
        return redirect('cursos')
    return redirect('home')

def home(request):
    slides = CarouselSlide.objects.all()
    return render(request, 'usuarios/home.html', {'slides': slides})