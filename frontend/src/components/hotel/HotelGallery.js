import React from 'react';

const HotelGallery = ({ images }) => (
  <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4">
    {images.map(image => (
      <img key={image.id} src={image.url} alt={image.alt_text || 'Hotel image'} className="w-full h-48 object-cover rounded" />
    ))}
  </div>
);

export default HotelGallery;