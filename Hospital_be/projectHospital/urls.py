"""projectHospital URL Configuration

Sistema de Hospitalización en Casa - API REST Endpoints
"""

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from appHospital import views


urlpatterns = [
    # Autenticación JWT
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Usuarios
    path("user/", views.ClaseCrearUsuarioView.as_view(), name="user-list-create"),
    path("user/me/", views.ClaseUserMeView.as_view(), name="user-me"),
    path("user/<int:pk>/", views.ClaseUserDetailView.as_view(), name="user-detail"),
    # Pacientes
    path(
        "paciente/", views.ClaseCrearPacienteView.as_view(), name="paciente-list-create"
    ),
    path(
        "paciente/<int:pk>/",
        views.ClasepacienteDetail.as_view(),
        name="paciente-detail",
    ),
    # Personal de Salud
    path(
        "personalSalud/",
        views.ClaseCrearPersonalSaludView.as_view(),
        name="personal-list-create",
    ),
    path(
        "personalSalud/<int:pk>/",
        views.ClasePersonalSaludDetail.as_view(),
        name="personal-detail",
    ),
    # Familiares
    path(
        "familiar/", views.ClaseCrearFamiliarView.as_view(), name="familiar-list-create"
    ),
    path(
        "familiar/<int:pk>/",
        views.ClaseFamiliarDetail.as_view(),
        name="familiar-detail",
    ),
    # Historias Clínicas
    path(
        "historia/",
        views.ClaseCrearHistoriaClinicaView.as_view(),
        name="historia-list-create",
    ),
    path(
        "historia/<int:pk>/",
        views.ClaseHistoriaClinicaDetail.as_view(),
        name="historia-detail",
    ),
    path(
        "paciente/<int:paciente_id>/historias/",
        views.ClasePacienteHistoriasView.as_view(),
        name="paciente-historias",
    ),
    # Signos Vitales
    path(
        "signos/",
        views.ClaseCrearSignosVitalesView.as_view(),
        name="signos-list-create",
    ),
    path(
        "signos/<int:pk>/",
        views.ClaseSignosVitalesDetail.as_view(),
        name="signos-detail",
    ),
    path(
        "paciente/<int:paciente_id>/signos/",
        views.ClasePacienteSignosView.as_view(),
        name="paciente-signos",
    ),
    path(
        "paciente/<int:paciente_id>/signos/ultimo/",
        views.ClasePacienteUltimoSignoView.as_view(),
        name="paciente-ultimo-signo",
    ),
]
