import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectHospital.settings")
django.setup()

from appHospital.models import ClaseUser

if not ClaseUser.objects.filter(username="admin").exists():
    ClaseUser.objects.create_superuser(
        username="admin",
        password="admin123",
        nombre="Admin",
        apellido="Sistema",
        perfil="admin",
        genero="O",
        telefono="0000000000",
    )
    print("Superusuario creado: admin / admin123")
else:
    print("El superusuario ya existe")
