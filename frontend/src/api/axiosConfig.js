import axios from 'axios';

const api = axios.create({
  // This pulls the value from your .env file
  baseURL: import.meta.env.VITE_API_BASE_URL, 
});

export default api;