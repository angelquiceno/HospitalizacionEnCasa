from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given username and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, password, **extra_fields)


class ClaseUser(AbstractBaseUser, PermissionsMixin):
    PERFIL_CHOICES = [
        ("personal_salud", "Personal de Salud"),
        ("familiar", "Familiar"),
        ("paciente", "Paciente"),
        ("admin", "Administrador"),
    ]

    GENERO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro"),
    ]

    id_user = models.AutoField(primary_key=True)
    username = models.CharField("Username", max_length=45, unique=True)
    password = models.CharField("Password", max_length=256)
    perfil = models.CharField("Perfil", max_length=45, choices=PERFIL_CHOICES)
    nombre = models.CharField("Nombre", max_length=45)
    apellido = models.CharField("Apellido", max_length=45)
    telefono = models.CharField("Telefono", max_length=45)
    genero = models.CharField("Genero", max_length=1, choices=GENERO_CHOICES)
    is_active = models.BooleanField("Activo", default=True)
    is_staff = models.BooleanField("Staff", default=False)

    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nombre", "apellido", "perfil"]

    def save(self, *args, **kwargs):
        # Solo hashear si la contraseña no está ya hasheada
        if self.password and not self.password.startswith("pbkdf2_"):
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} - {self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
