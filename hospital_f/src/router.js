import { createRouter, createWebHistory } from "vue-router";
import authService from "./services/auth.service";

// Importar componentes
import LogIn from "./components/LogIn.vue";
import SignUp from "./components/SignUp.vue";

const routes = [
  {
    path: "/",
    name: "login",
    component: LogIn,
    meta: { requiresAuth: false },
  },
  {
    path: "/registro",
    name: "signup",
    component: SignUp,
    meta: { requiresAuth: false },
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: () => import("./components/dashboard/Dashboard.vue"),
    meta: { requiresAuth: true },
    children: [
      {
        path: "",
        name: "home",
        component: () => import("./components/dashboard/Home.vue"),
      },
      {
        path: "pacientes",
        name: "pacientes",
        component: () => import("./components/pacientes/PacienteList.vue"),
      },
      {
        path: "pacientes/nuevo",
        name: "paciente-nuevo",
        component: () => import("./components/pacientes/PacienteForm.vue"),
      },
      {
        path: "pacientes/:id",
        name: "paciente-detalle",
        component: () => import("./components/pacientes/PacienteDetail.vue"),
      },
      {
        path: "pacientes/:id/editar",
        name: "paciente-editar",
        component: () => import("./components/pacientes/PacienteForm.vue"),
      },
      {
        path: "personal",
        name: "personal",
        component: () => import("./components/personal/PersonalList.vue"),
      },
      {
        path: "personal/nuevo",
        name: "personal-nuevo",
        component: () => import("./components/personal/PersonalForm.vue"),
      },
      {
        path: "personal/:id",
        name: "personal-detalle",
        component: () => import("./components/personal/PersonalDetail.vue"),
      },
      {
        path: "familiares",
        name: "familiares",
        component: () => import("./components/familiares/FamiliarList.vue"),
      },
      {
        path: "familiares/nuevo",
        name: "familiar-nuevo",
        component: () => import("./components/familiares/FamiliarForm.vue"),
      },
      {
        path: "historias",
        name: "historias",
        component: () => import("./components/historias/HistoriaList.vue"),
      },
      {
        path: "historias/nueva",
        name: "historia-nueva",
        component: () => import("./components/historias/HistoriaForm.vue"),
      },
      {
        path: "signos",
        name: "signos",
        component: () => import("./components/signos/SignosList.vue"),
      },
      {
        path: "signos/nuevo",
        name: "signos-nuevo",
        component: () => import("./components/signos/SignosForm.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation guard para proteger rutas
router.beforeEach((to, from, next) => {
  const isAuthenticated = authService.isAuthenticated();
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);

  if (requiresAuth && !isAuthenticated) {
    // Ruta requiere autenticación pero el usuario no está autenticado
    next({ name: "login" });
  } else if (!requiresAuth && isAuthenticated && (to.name === "login" || to.name === "signup")) {
    // Usuario autenticado intenta acceder a login o signup
    next({ name: "dashboard" });
  } else {
    // Permitir navegación
    next();
  }
});

export default router;
