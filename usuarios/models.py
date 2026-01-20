from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    ROLES = (
        ('estudiante', 'Estudiante'),
        ('docente', 'Docente'),
    )

    rol = models.CharField(
        max_length=20,
        choices=ROLES,
        default='estudiante'
    )

    def __str__(self):
        return f"{self.username} ({self.rol})"


class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    docente = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'rol': 'docente'}
    )

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class CarouselSlide(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    promo_text = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='carousel/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
