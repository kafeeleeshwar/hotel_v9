import React from 'react';
import HotelCard from './HotelCard';
import Loading from '../common/Loading';

const HotelList = ({ hotels, loading }) => {
  if (loading) return <Loading />;
  if (!hotels.length) return <p>No hotels found.</p>;

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      {hotels.map(hotel => (
        <HotelCard key={hotel.id} hotel={hotel} />
      ))}
    </div>
  );
};

export default HotelList;