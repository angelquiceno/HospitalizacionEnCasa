# Plan de Implementación

- [x] 1. Configurar archivos de entorno y seguridad


  - Crear archivo .env.example con template de variables de entorno
  - Crear archivo .gitignore completo para Python y Node.js
  - Actualizar settings.py para usar variables de entorno en SECRET_KEY y DATABASE
  - _Requisitos: 8.2, 8.3, 8.4_

- [x] 2. Corregir modelo de Usuario y autenticación


  - Eliminar salt hardcodeado en user.py y usar hash correcto de Django
  - Agregar validaciones y choices para campos perfil y genero
  - Agregar campo is_active al modelo ClaseUser
  - _Requisitos: 1.2, 1.5_

- [x] 3. Mejorar modelos existentes con validaciones



  - Actualizar ClasePaciente: aumentar max_length de direccion, agregar validación de edad
  - Actualizar ClaseFamiliar: cambiar email a EmailField, agregar choices para parentezco
  - Actualizar ClaseHistoriaClinica: cambiar CharField a TextField para campos largos, agregar auto_now_add
  - Actualizar ClaseSignosVitales: agregar validadores de rango para signos vitales
  - _Requisitos: 3.2, 4.2, 5.2, 6.2, 6.4_

- [x] 4. Completar serializers con validaciones


  - Revisar y mejorar serializers existentes (User, Paciente, PersonalSalud)
  - Crear FamiliarSerializer completo con validaciones
  - Crear HistoriaClinicaSerializer completo con validaciones
  - Crear SignosVitalesSerializer completo con validaciones
  - _Requisitos: 9.1, 9.3_

- [x] 5. Implementar vistas CRUD para Usuarios


  - Agregar método GET (list) a usuarioCreateView
  - Agregar métodos PUT y DELETE a usuarioDetail
  - Crear endpoint /user/me/ para obtener usuario actual
  - _Requisitos: 1.4, 10.1, 10.2_

- [x] 6. Completar vistas CRUD para Pacientes


  - Agregar método GET (list) a PacienteCreateView
  - Agregar métodos PUT y DELETE a PacienteDetail
  - _Requisitos: 3.3, 3.4, 10.1, 10.2_

- [x] 7. Completar vistas CRUD para Personal de Salud


  - Agregar método GET (list) a PersonalSaludCreateView
  - Agregar métodos PUT y DELETE a PersonalSaludDetail
  - _Requisitos: 2.2, 2.4, 2.5, 10.1, 10.2_

- [x] 8. Implementar vistas CRUD completas para Familiares


  - Crear vista list/create para Familiares
  - Crear vista retrieve/update/delete para Familiar individual
  - Agregar endpoints en urls.py
  - _Requisitos: 4.3, 4.4, 10.1, 10.2_

- [x] 9. Implementar vistas CRUD completas para Historias Clínicas


  - Crear vista list/create para Historias Clínicas
  - Crear vista retrieve/update/delete para Historia individual
  - Crear endpoint para listar historias de un paciente específico
  - Agregar endpoints en urls.py
  - _Requisitos: 5.3, 5.4, 5.5, 10.1, 10.2_

- [x] 10. Implementar vistas CRUD completas para Signos Vitales


  - Crear vista list/create para Signos Vitales
  - Crear vista retrieve/update/delete para Signos individual
  - Crear endpoint para listar signos de un paciente específico
  - Crear endpoint para obtener último registro de signos de un paciente
  - Agregar endpoints en urls.py
  - _Requisitos: 6.3, 6.5, 10.1, 10.2_

- [x] 11. Actualizar urls.py con todos los endpoints



  - Agregar rutas faltantes para Familiares
  - Agregar rutas faltantes para Historias Clínicas
  - Agregar rutas faltantes para Signos Vitales
  - Agregar rutas de listado para entidades existentes
  - Organizar URLs de forma consistente
  - _Requisitos: 10.1, 10.2, 10.4_

- [x] 12. Crear servicios API en el frontend


  - Crear api.js con cliente Axios base y configuración de interceptores
  - Crear auth.service.js con funciones de login, logout, registro
  - Crear paciente.service.js con funciones CRUD de pacientes
  - Crear personal.service.js con funciones CRUD de personal
  - Crear familiar.service.js con funciones CRUD de familiares
  - Crear historia.service.js con funciones CRUD de historias
  - Crear signos.service.js con funciones CRUD de signos vitales
  - _Requisitos: 7.3, 10.3_

- [x] 13. Corregir y mejorar componente LogIn


  - Corregir URL del backend (eliminar URL hardcodeada de Heroku)
  - Usar servicio de autenticación en lugar de Axios directo
  - Mejorar manejo de errores y mensajes al usuario
  - Guardar tokens en localStorage correctamente
  - _Requisitos: 1.1, 7.3, 9.4_

- [x] 14. Crear componente SignUp para registro


  - Crear formulario de registro con todos los campos de usuario
  - Implementar validaciones en el formulario
  - Conectar con servicio de autenticación
  - Agregar manejo de errores
  - _Requisitos: 1.2, 7.1, 9.4_

- [x] 15. Implementar router con guards de autenticación



  - Expandir router.js con rutas para todos los módulos
  - Implementar navigation guards para proteger rutas
  - Configurar redirecciones según autenticación
  - _Requisitos: 7.2, 7.3_

- [x] 16. Crear componentes de layout (Navbar y Sidebar)


  - Crear Navbar.vue con navegación principal y logout
  - Crear Sidebar.vue con menú de módulos
  - Integrar en App.vue
  - _Requisitos: 7.2, 7.4_

- [x] 17. Crear Dashboard y Home


  - Crear Dashboard.vue como contenedor principal
  - Crear Home.vue con vista de bienvenida y resumen
  - Mostrar información según perfil de usuario
  - _Requisitos: 7.2_

- [x] 18. Implementar módulo de gestión de Pacientes


  - Crear PacienteList.vue para listar pacientes
  - Crear PacienteForm.vue para crear/editar pacientes
  - Crear PacienteDetail.vue para ver detalle de paciente
  - Conectar con servicio de pacientes
  - _Requisitos: 3.3, 3.4, 3.5, 7.4_

- [x] 19. Implementar módulo de gestión de Personal de Salud


  - Crear PersonalList.vue para listar personal
  - Crear PersonalForm.vue para crear/editar personal
  - Crear PersonalDetail.vue para ver detalle de personal
  - Conectar con servicio de personal
  - _Requisitos: 2.2, 2.3, 2.4, 7.4_

- [x] 20. Implementar módulo de gestión de Familiares

  - Crear FamiliarList.vue para listar familiares
  - Crear FamiliarForm.vue para crear/editar familiares
  - Crear FamiliarDetail.vue para ver detalle de familiar
  - Conectar con servicio de familiares
  - _Requisitos: 4.3, 4.4, 7.4_

- [x] 21. Implementar módulo de Historias Clínicas

  - Crear HistoriaList.vue para listar historias de un paciente
  - Crear HistoriaForm.vue para crear/editar historias
  - Crear HistoriaDetail.vue para ver detalle de historia
  - Conectar con servicio de historias
  - _Requisitos: 5.3, 5.4, 7.4_

- [x] 22. Implementar módulo de Signos Vitales

  - Crear SignosForm.vue para registrar signos vitales
  - Crear SignosList.vue para listar signos de un paciente
  - Crear SignosChart.vue para visualizar evolución (gráfica simple)
  - Conectar con servicio de signos vitales
  - _Requisitos: 6.3, 6.5, 7.4_

- [x] 23. Implementar manejo de errores global

  - Agregar interceptor de errores en api.js
  - Crear componente o sistema de notificaciones para mostrar errores
  - Manejar errores 401 redirigiendo a login
  - Manejar errores de red
  - _Requisitos: 9.1, 9.2, 9.4, 9.5_

- [x] 24. Crear documentación README


  - Crear README.md con descripción del proyecto
  - Agregar instrucciones de instalación para backend
  - Agregar instrucciones de instalación para frontend
  - Agregar instrucciones para ejecutar en desarrollo
  - Documentar estructura del proyecto
  - Agregar información sobre variables de entorno
  - _Requisitos: 8.1_

- [x] 25. Crear scripts de inicialización


  - Crear script para ejecutar migraciones
  - Crear script para crear superusuario
  - Crear management command para cargar datos de prueba
  - _Requisitos: 8.5_
