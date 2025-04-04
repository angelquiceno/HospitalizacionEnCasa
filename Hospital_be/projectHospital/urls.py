"""projectHospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from appHospital import views
from appHospital.views.PersonalSaludCreateView import ClaseCrearPersonalSaludView
from appHospital.views.PersonalSaludDetail import ClasePersonalSaludDetail


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('paciente/', views.ClaseCrearPacienteView.as_view()),
    path('paciente/<int:pk>/', views.ClasepacienteDetail.as_view()),
    path('user/', views.ClaseCrearUsuarioView.as_view()),
    path('user/<int:pk>', views.ClaseUserDetailView.as_view()),
    path('personalSalud/', views.ClaseCrearPersonalSaludView.as_view()),
    path('personalSalud/<int:pk>', views.ClasePersonalSaludDetail.as_view())



]

