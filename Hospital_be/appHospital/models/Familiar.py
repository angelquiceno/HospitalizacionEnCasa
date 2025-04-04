from django.db import models
from .user import ClaseUser
from .Paciente import ClasePaciente

class ClaseFamiliar(models.Model):
    id_Familiar=models.AutoField(primary_key=True)
    id_user=models.ForeignKey(ClaseUser, related_name='Familiar', on_delete=models.CASCADE)
    id_Paciente=models.ForeignKey(ClasePaciente, related_name= 'Familiar', on_delete=models.CASCADE)
    email=models.CharField('Email', max_length=45)
    parentezco=models.CharField('Parentezco', max_length=45)
   
   
    
