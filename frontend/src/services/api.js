import { getToken } from './auth';

export const apiRequest = async (endpoint, method = 'GET', body = null, params = {}) => {
  const url = new URL(`http://localhost:8000${endpoint}`);
  Object.keys(params).forEach(key => url.searchParams.append(key, params[key]));

  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${getToken()}`
  };

  const config = { method, headers };
  if (body) {
    config.body = JSON.stringify(body);
  }

  const response = await fetch(url, config);
  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.detail || 'API request failed');
  }

  return data;
};