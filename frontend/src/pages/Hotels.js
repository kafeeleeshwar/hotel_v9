import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { searchHotels } from '../services/hotels';
import HotelList from '../components/hotel/HotelList';
import SearchForm from '../components/forms/SearchForm';
import Loading from '../components/common/Loading';

const Hotels = () => {
  const [hotels, setHotels] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const location = useLocation();

  useEffect(() => {
    const fetchHotels = async () => {
      setLoading(true);
      try {
        const params = new URLSearchParams(location.search);
        const data = await searchHotels(Object.fromEntries(params));
        setHotels(data.hotels);
      } catch (err) {
        setError(err.message || 'Failed to fetch hotels');
      } finally {
        setLoading(false);
      }
    };
    fetchHotels();
  }, [location.search]);

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold">Hotels</h1>
      <SearchForm />
      {error && <p className="text-red-600 mt-4">{error}</p>}
      <HotelList hotels={hotels} loading={loading} />
    </div>
  );
};

export default Hotels;