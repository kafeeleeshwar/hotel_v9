import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getHotelById } from '../../services/hotels';
import Loading from '../common/Loading';
import BookingForm from '../forms/BookingForm';
import HotelGallery from './HotelGallery';

const HotelDetails = () => {
  const { hotelId } = useParams();
  const [hotel, setHotel] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchHotel = async () => {
      try {
        const data = await getHotelById(hotelId);
        setHotel(data);
      } catch (err) {
        setError(err.message || 'Failed to fetch hotel details');
      } finally {
        setLoading(false);
      }
    };
    fetchHotel();
  }, [hotelId]);

  if (loading) return <Loading />;
  if (error) return <p className="text-red-600">{error}</p>;
  if (!hotel) return <p>Hotel not found.</p>;

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold">{hotel.name}</h1>
      <p className="text-gray-600">{hotel.city}, {hotel.country}</p>
      <HotelGallery images={hotel.images} />
      <p className="mt-4">{hotel.description}</p>
      <div className="mt-4">
        <h2 className="text-xl font-semibold">Available Rooms</h2>
        {hotel.rooms.map(room => (
          <div key={room.id} className="border p-4 rounded mt-2">
            <h3>{room.name} ({room.room_type})</h3>
            <p>${room.base_price}/night</p>
            <BookingForm hotelId={hotel.id} roomId={room.id} />
          </div>
        ))}
      </div>
    </div>
  );
};

export default HotelDetails;