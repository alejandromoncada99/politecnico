from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="Alejandro",
                email="alejandromoncadaroman2@gmail.com",
                password=os.getenv("ADMIN_PASSWORD", "AlejoMoncada16")
            )
            self.stdout.write("Superusuario creado")
        else:
            self.stdout.write("Superusuario ya existe")
