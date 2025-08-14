import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Input from '../ui/Input';
import Button from '../ui/Button';

const SearchForm = () => {
  const [formData, setFormData] = useState({
    destination: '',
    check_in_date: '',
    check_out_date: '',
    guests: 1
  });
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    const params = new URLSearchParams(formData);
    navigate(`/hotels?${params.toString()}`);
  };

  return (
    <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-4 gap-4">
      <Input
        type="text"
        placeholder="Destination"
        value={formData.destination}
        onChange={(e) => setFormData({ ...formData, destination: e.target.value })}
      />
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
      <Button type="submit" className="col-span-1">Search</Button>
    </form>
  );
};

export default SearchForm;