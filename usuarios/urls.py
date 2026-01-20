from django.urls import path
from . import views
from usuarios.views import home
urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('contacto/', views.contacto, name='contacto'),

    # Redirección por rol
    path('redireccion/', views.redireccion_por_rol, name='redireccion_por_rol'),

    # Dashboards
    path('docente/crear-curso/', views.crear_curso, name='crear_curso'),
    path('estudiante/cursos/', views.cursos_disponibles, name='cursos'),
]
