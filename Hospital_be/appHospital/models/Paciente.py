from django.db import models
from .user import ClaseUser
from .PersonalSalud import clasePersonalSalud

class ClasePaciente(models.Model):
    id_Paciente=models.AutoField(primary_key=True)
    id_PersonalSalud=models.ForeignKey(clasePersonalSalud, related_name= 'Paciente', on_delete=models.CASCADE)
    id_user=models.ForeignKey(ClaseUser, related_name='Paciente', on_delete=models.CASCADE)
    direccion=models.CharField('Direccion', max_length=45)
    ciudad=models.CharField('Ciudad', max_length=45)
    fecha_nacimiento=models.DateField()
    



