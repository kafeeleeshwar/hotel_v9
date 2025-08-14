import { apiRequest } from './api';

export const createPaymentIntent = (bookingId) => {
  return apiRequest('/api/payments/create-payment-intent', 'POST', { booking_id: bookingId });
};