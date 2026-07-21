import axios from 'axios';

// Instancia global de Axios apuntando al backend
export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor de Peticiones (Request)
// Intercepta cada llamada saliente e inyecta el token JWT si existe en el almacenamiento
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Interceptor de Respuestas (Response)
// Captura errores globales como un token expirado (401)
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      // Limpia el estado local y redirige si las credenciales expiraron
      localStorage.removeItem('access_token');
      // Opcional: window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);