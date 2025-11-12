import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectHospital.settings")
django.setup()

from appHospital.models import ClaseUser

# Crear usuario de prueba
if not ClaseUser.objects.filter(username="test").exists():
    user = ClaseUser.objects.create_user(
        username="test",
        password="test123",
        nombre="Usuario",
        apellido="Prueba",
        perfil="personal_salud",
        genero="M",
        telefono="1234567890",
    )
    print("Usuario de prueba creado:")
    print("Usuario: test")
    print("Contraseña: test123")
else:
    print("El usuario test ya existe")

# Verificar admin
admin = ClaseUser.objects.filter(username="admin").first()
if admin:
    print(f"\nUsuario admin existe:")
    print(f"Username: {admin.username}")
    print(f"Perfil: {admin.perfil}")
    print(f"Activo: {admin.is_active}")
