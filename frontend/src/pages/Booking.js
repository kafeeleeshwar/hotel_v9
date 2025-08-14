import React, { useContext } from 'react';
import { BookingContext } from '../context/BookingContext';
import { useNavigate } from 'react-router-dom';

const Booking = () => {
  const { booking } = useContext(BookingContext);
  const navigate = useNavigate();

  if (!booking) {
    navigate('/hotels');
    return null;
  }

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold">Booking Confirmation</h1>
      <p>Booking Reference: {booking.booking_reference}</p>
      <p>Hotel: {booking.hotel.name}</p>
      <p>Room: {booking.room.name}</p>
      <p>Total Amount: ${booking.total_amount}</p>
    </div>
  );
};

export default Booking;