@echo off
echo ========================================
echo  Reiniciando Base de Datos
echo ========================================
echo.
echo IMPORTANTE: Asegurate de cerrar el servidor backend primero!
echo.
pause

cd Hospital_be

echo Eliminando base de datos antigua...
del db.sqlite3

echo Creando nueva base de datos...
python manage.py migrate

echo Creando superusuario...
python create_superuser.py

echo Creando usuario de prueba...
python create_test_user.py

echo.
echo ========================================
echo  Base de datos reiniciada!
echo ========================================
echo.
echo Usuarios disponibles:
echo 1. admin / admin123
echo 2. test / test123
echo.
echo Ahora ejecuta: start_servers.bat
echo.
pause
