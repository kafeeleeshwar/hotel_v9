import { apiRequest } from './api';

export const createBooking = (data) => {
  return apiRequest('/api/bookings/', 'POST', data);
};

export const getUserBookings = () => {
  return apiRequest('/api/bookings/', 'GET');
};