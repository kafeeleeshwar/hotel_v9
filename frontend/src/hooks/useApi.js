import { useState } from 'react';
import { apiRequest } from '../services/api';

const useApi = (endpoint, method = 'GET') => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchData = async (body = null, params = {}) => {
    setLoading(true);
    try {
      const response = await apiRequest(endpoint, method, body, params);
      setData(response);
      return response;
    } catch (err) {
      setError(err.message || 'API request failed');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return { data, loading, error, fetchData };
};

export default useApi;