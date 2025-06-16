import { reactive, readonly } from 'vue';

const state = reactive({
  isAuthenticated: !!localStorage.getItem('accessToken'),
  accessToken: localStorage.getItem('accessToken'),
  refreshToken: localStorage.getItem('refreshToken'),
});

const login = (access, refresh) => {
  localStorage.setItem('accessToken', access);
  localStorage.setItem('refreshToken', refresh);
  state.accessToken = access;
  state.refreshToken = refresh;
  state.isAuthenticated = true;
};

const logout = () => {
  localStorage.removeItem('accessToken');
  localStorage.removeItem('refreshToken');
  state.accessToken = null;
  state.refreshToken = null;
  state.isAuthenticated = false;

};


export const useAuthStore = () => {
  return {
    state: readonly(state),
    login,
    logout,
  };
};