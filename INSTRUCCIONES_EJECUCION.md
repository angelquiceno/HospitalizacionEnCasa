# Instrucciones para Ejecutar el Proyecto

## ✅ Todo está configurado y listo

El proyecto está completamente configurado con:
- Base de datos SQLite creada y migrada
- Superusuario creado
- Dependencias instaladas

## 🚀 Para ejecutar el proyecto:

### Opción 1: Dos terminales separadas (RECOMENDADO)

**Terminal 1 - Backend:**
```bash
cd Hospital_be
python manage.py runserver
```
El backend estará en: http://localhost:8000

**Terminal 2 - Frontend:**
```bash
cd hospital_f
npm run serve
```
El frontend estará en: http://localhost:8080

### Opción 2: Usar el script de inicio

**Windows:**
```bash
start_servers.bat
```

## 🔐 Credenciales de acceso

**Superusuario (para admin de Django):**
- Usuario: `admin`
- Contraseña: `admin123`
- URL: http://localhost:8000/admin

**Para la aplicación:**
Puedes registrarte desde: http://localhost:8080
O usar el superusuario creado.

## 📝 Notas importantes

1. El backend usa SQLite (archivo `Hospital_be/db.sqlite3`)
2. No necesitas PostgreSQL instalado
3. Todos los cambios se guardan en la base de datos local
4. Para crear más usuarios, usa el formulario de registro en la app

## 🎯 Próximos pasos

1. Abre http://localhost:8080 en tu navegador
2. Regístrate o inicia sesión
3. Explora los módulos:
   - Pacientes
   - Personal de Salud
   - Familiares
   - Historias Clínicas
   - Signos Vitales

¡Disfruta tu aplicación!
