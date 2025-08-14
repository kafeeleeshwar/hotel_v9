import React, { createContext, useState } from 'react';
import useLocalStorage from '../hooks/useLocalStorage';

export const BookingContext = createContext();

export const BookingProvider = ({ children }) => {
  const [booking, setBooking] = useLocalStorage('booking', null);

  return (
    <BookingContext.Provider value={{ booking, setBooking }}>
      {children}
    </BookingContext.Provider>
  );
};