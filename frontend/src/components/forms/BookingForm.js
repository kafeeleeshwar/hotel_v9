import React, { useState, useContext } from 'react';
import { BookingContext } from '../../context/BookingContext';
import Input from '../ui/Input';
import Button from '../ui/Button';
import { createBooking } from '../../services/bookings';

const BookingForm = ({ hotelId, roomId }) => {
  const { setBooking } = useContext(BookingContext);
  const [formData, setFormData] = useState({
    check_in_date: '',
    check_out_date: '',
    guests: 1,
    special_requests: ''
  });
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const booking = await createBooking({ ...formData, hotel_id: hotelId, room_id: roomId });
      setBooking(booking);
    } catch (err) {
      setError(err.message || 'Booking failed');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      {error && <p className="text-red-600">{error}</p>}
      <Input
        type="date"
        value={formData.check_in_date}
        onChange={(e) => setFormData({ ...formData, check_in_date: e.target.value })}
      />
      <Input
        type="date"
        value={formData.check_out_date}
        onChange={(e) => setFormData({ ...formData, check_out_date: e.target.value })}
      />
      <Input
        type="number"
        placeholder="Guests"
        value={formData.guests}
        onChange={(e) => setFormData({ ...formData, guests: parseInt(e.target.value) })}
        min="1"
      />
      <Input
        type="text"
        placeholder="Special Requests"
        value={formData.special_requests}
        onChange={(e) => setFormData({ ...formData, special_requests: e.target.value })}
      />
      <Button type="submit" className="w-full">Book Now</Button>
    </form>
  );
};

export default BookingForm;