from django.db import models
from .user import ClaseUser

class clasePersonalSalud(models.Model):
    id_PersonalSalud=models.AutoField(primary_key=True)
    id_user=models.ForeignKey(ClaseUser,related_name='PersonalSalud', on_delete=models.CASCADE)
    rol=models.CharField('Rol',max_length=45)
    especialidad=models.CharField('Especialidad', max_length=45)
