import { ref } from 'vue';


const theme = ref('light');

const applyTheme = (newTheme) => {
  theme.value = newTheme;

  localStorage.setItem('theme', newTheme);
 
  if (newTheme === 'dark') {
    document.body.classList.add('dark-theme');
  } else {
    document.body.classList.remove('dark-theme');
  }
};

const toggleTheme = () => {
  const newTheme = theme.value === 'light' ? 'dark' : 'light';
  applyTheme(newTheme);
};


const initializeTheme = () => {
  const savedTheme = localStorage.getItem('theme');

  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

  if (savedTheme) {
    applyTheme(savedTheme);
  } else if (prefersDark) {
    applyTheme('dark');
  } else {
    applyTheme('light');
  }
};


export const useThemeStore = () => {
  return {
    theme,
    toggleTheme,
    initializeTheme,
  };
};