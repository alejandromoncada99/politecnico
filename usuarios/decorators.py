from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import wraps

def rol_requerido(roles_permitidos):
    """
    Permite el acceso solo si el usuario pertenece a uno de los grupos indicados.
    roles_permitidos = ['docente', 'estudiante']
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            # Debug temporal
            print("USUARIO:", request.user.username)
            print("GRUPOS:", list(request.user.groups.values_list('name', flat=True)))

            # Validar grupos
            if request.user.groups.filter(name__in=roles_permitidos).exists():
                return view_func(request, *args, **kwargs)

            # Si no tiene permisos, redirigir al home
            return redirect('home')

        return _wrapped_view
    return decorator
