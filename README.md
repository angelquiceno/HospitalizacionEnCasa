# Sistema de Hospitalización en Casa

Sistema completo de gestión hospitalaria domiciliaria desarrollado con Django REST Framework y Vue.js 3.

## Descripción

Aplicación web full-stack para gestionar la atención médica en casa, permitiendo el registro y seguimiento de pacientes, personal de salud, familiares, historias clínicas y signos vitales.

## Tecnologías

### Backend
- Django 4.1
- Django REST Framework 3.13.1
- PostgreSQL
- JWT Authentication (djangorestframework-simplejwt)
- Python 3.8+

### Frontend
- Vue.js 3.2.13
- Vue Router 4.0.3
- Axios 0.27.2

## Estructura del Proyecto

```
HospitalizacionEnCasa/
├── Hospital_be/          # Backend Django
│   ├── appHospital/      # Aplicación principal
│   │   ├── models/       # Modelos de datos
│   │   ├── serializers/  # Serializers DRF
│   │   └── views/        # Vistas API
│   ├── projectHospital/  # Configuración del proyecto
│   ├── .env              # Variables de entorno
│   └── requirements.txt  # Dependencias Python
│
└── hospital_f/           # Frontend Vue.js
    ├── src/
    │   ├── components/   # Componentes Vue
    │   ├── services/     # Servicios API
    │   └── router.js     # Configuración de rutas
    └── package.json      # Dependencias Node.js
```

## ✅ Instalación Completada

**El proyecto ya está configurado y listo para usar.**

### Requisitos
- Python 3.8+ (ya instalado)
- Node.js 14+ (ya instalado)
- ✅ Base de datos SQLite (ya configurada)
- ✅ Dependencias instaladas
- ✅ Migraciones aplicadas
- ✅ Superusuario creado

## 🚀 Ejecutar el Proyecto

### Opción 1: Script Automático (Recomendado)
```bash
start_servers.bat
```

### Opción 2: Manual (Dos terminales)

**Terminal 1 - Backend:**
```bash
cd Hospital_be
python manage.py runserver
```

**Terminal 2 - Frontend:**
```bash
cd hospital_f
npm run serve
```

### Acceso
- **Frontend:** http://localhost:8080
- **Backend API:** http://localhost:8000
- **Admin Django:** http://localhost:8000/admin

### Credenciales
- **Usuario:** admin
- **Contraseña:** admin123

## API Endpoints

### Autenticación
- `POST /login/` - Iniciar sesión
- `POST /refresh/` - Refrescar token

### Usuarios
- `GET /user/` - Listar usuarios
- `POST /user/` - Crear usuario
- `GET /user/me/` - Usuario actual
- `GET /user/<id>/` - Detalle de usuario
- `PUT /user/<id>/` - Actualizar usuario
- `DELETE /user/<id>/` - Eliminar usuario

### Pacientes
- `GET /paciente/` - Listar pacientes
- `POST /paciente/` - Crear paciente
- `GET /paciente/<id>/` - Detalle de paciente
- `PUT /paciente/<id>/` - Actualizar paciente
- `DELETE /paciente/<id>/` - Eliminar paciente
- `GET /paciente/<id>/historias/` - Historias del paciente
- `GET /paciente/<id>/signos/` - Signos vitales del paciente
- `GET /paciente/<id>/signos/ultimo/` - Último signo vital

### Personal de Salud
- `GET /personalSalud/` - Listar personal
- `POST /personalSalud/` - Crear personal
- `GET /personalSalud/<id>/` - Detalle de personal
- `PUT /personalSalud/<id>/` - Actualizar personal
- `DELETE /personalSalud/<id>/` - Eliminar personal

### Familiares
- `GET /familiar/` - Listar familiares
- `POST /familiar/` - Crear familiar
- `GET /familiar/<id>/` - Detalle de familiar
- `PUT /familiar/<id>/` - Actualizar familiar
- `DELETE /familiar/<id>/` - Eliminar familiar

### Historias Clínicas
- `GET /historia/` - Listar historias
- `POST /historia/` - Crear historia
- `GET /historia/<id>/` - Detalle de historia
- `PUT /historia/<id>/` - Actualizar historia
- `DELETE /historia/<id>/` - Eliminar historia

### Signos Vitales
- `GET /signos/` - Listar signos
- `POST /signos/` - Crear signos
- `GET /signos/<id>/` - Detalle de signos
- `PUT /signos/<id>/` - Actualizar signos
- `DELETE /signos/<id>/` - Eliminar signos

## Uso

1. Acceder a `http://localhost:8080`
2. Registrarse o iniciar sesión
3. Navegar por los diferentes módulos:
   - **Inicio**: Dashboard con estadísticas
   - **Pacientes**: Gestión de pacientes
   - **Personal de Salud**: Gestión de personal médico
   - **Familiares**: Gestión de familiares de pacientes
   - **Historias Clínicas**: Registro de diagnósticos y tratamientos
   - **Signos Vitales**: Monitoreo de signos vitales

## Características

- ✅ Autenticación JWT con refresh tokens
- ✅ CRUD completo para todas las entidades
- ✅ Validaciones en backend y frontend
- ✅ Interfaz responsive
- ✅ Manejo de errores
- ✅ Relaciones entre entidades
- ✅ Dashboard con estadísticas
- ✅ Navegación protegida con guards

## Desarrollo

### Ejecutar tests (Backend)
```bash
cd Hospital_be
python manage.py test
```

### Build para producción (Frontend)
```bash
cd hospital_f
npm run build
```

## Contribuir

Este es un proyecto académico. Para contribuir:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Crea un Pull Request

## Licencia

Proyecto académico - Hospital en Casa G2 2025

## Contacto

Para preguntas o soporte, contactar al equipo de desarrollo.
