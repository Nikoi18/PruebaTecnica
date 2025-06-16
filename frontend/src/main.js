import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { useThemeStore } from './store/theme'

const { initializeTheme } = useThemeStore();
initializeTheme();

createApp(App).use(router).mount('#app')