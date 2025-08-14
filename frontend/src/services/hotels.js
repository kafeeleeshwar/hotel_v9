import { apiRequest } from './api';

export const searchHotels = (params) => {
  return apiRequest('/api/hotels/search', 'GET', null, params);
};

export const getHotelById = (hotelId) => {
  return apiRequest(`/api/hotels/${hotelId}`, 'GET');
};