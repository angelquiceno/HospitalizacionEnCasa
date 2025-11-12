@echo off
echo ========================================
echo  Sistema de Hospitalizacion en Casa
echo ========================================
echo.
echo Iniciando servidores...
echo.

echo [1/2] Iniciando Backend (Django)...
start "Backend - Django" cmd /k "cd Hospital_be && python manage.py runserver"

timeout /t 3 /nobreak > nul

echo [2/2] Iniciando Frontend (Vue.js)...
start "Frontend - Vue.js" cmd /k "cd hospital_f && npm run serve"

echo.
echo ========================================
echo  Servidores iniciados!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:8080
echo.
echo Presiona cualquier tecla para salir...
pause > nul
