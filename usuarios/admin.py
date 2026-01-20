from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Curso
from .models import CarouselSlide

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario

    list_display = ('username', 'email', 'rol', 'is_staff', 'is_active')
    list_filter = ('rol', 'is_staff', 'is_active')

    fieldsets = UserAdmin.fieldsets + (
        ('Rol del usuario', {'fields': ('rol',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rol del usuario', {'fields': ('rol',)}),
    )


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'docente', 'activo')
    list_filter = ('activo',)

@admin.register(CarouselSlide)
class CarouselSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
