import React from 'react';
import { Link } from 'react-router-dom';
import Card from '../ui/Card';
import Badge from '../ui/Badge';

const HotelCard = ({ hotel }) => (
  <Card>
    <img src={hotel.images[0]?.url || 'https://placehold.co/300x200'} alt={hotel.name} className="w-full h-48 object-cover rounded-t-lg" />
    <div className="p-4">
      <h3 className="text-lg font-semibold">{hotel.name}</h3>
      <p className="text-gray-600">{hotel.city}, {hotel.country}</p>
      <div className="flex items-center mt-2">
        {[...Array(hotel.star_rating)].map((_, i) => (
          <span key={i} className="text-yellow-500">★</span>
        ))}
      </div>
      <Badge>{hotel.average_rating ? `${hotel.average_rating}/5` : 'No reviews'}</Badge>
      <Link to={`/hotels/${hotel.id}`} className="mt-4 block text-blue-600 hover:underline">View Details</Link>
    </div>
  </Card>
);

export default HotelCard;