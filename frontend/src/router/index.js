
import { createRouter, createWebHistory } from 'vue-router';
import InventoryManager from '../components/InventoryManager.vue';
import LoginView from '../views/LoginView.vue';
import { useAuthStore } from '../store/auth';

const routes = [
  {
    path: '/',
    name: 'Inventory',
    component: InventoryManager,
    meta: { requiresAuth: true },
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});


router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);

  if (requiresAuth && !authStore.state.isAuthenticated) {
    next('/login');
  } else {
    next(); 
  }
});

export default router;