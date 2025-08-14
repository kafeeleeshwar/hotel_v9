import { apiRequest } from './api';

let token = null;

export const setToken = (newToken) => {
  token = newToken;
};

export const getToken = () => token;

export const login = async ({ username, password }) => {
  const formData = new URLSearchParams({ username, password });
  const response = await fetch('http://localhost:8000/api/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: formData
  });
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.detail || 'Login failed');
  }
  setToken(data.access_token);
  return { access_token: data.access_token, user: data.user };
};

export const register = async (data) => {
  return apiRequest('/api/auth/register', 'POST', data);
};