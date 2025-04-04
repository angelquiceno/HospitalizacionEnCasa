from django.contrib import admin
from .models.user import ClaseUser
from .models.Familiar import ClaseFamiliar
from .models.Paciente import ClasePaciente
from .models.PersonalSalud import clasePersonalSalud
from .models.HistoriaClinica import ClaseHistoriaClinica
from .models.SignosVitales import ClaseSignosVitales

admin.site.register(ClaseFamiliar)
admin.site.register(ClasePaciente)
admin.site.register(clasePersonalSalud)
admin.site.register(ClaseSignosVitales)
admin.site.register(ClaseHistoriaClinica)
admin.site.register(ClaseUser)

# Register your models here.
