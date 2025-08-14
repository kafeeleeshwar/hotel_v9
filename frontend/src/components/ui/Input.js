import React from 'react';

const Input = ({ className = '', ...props }) => (
  <input
    className={`border p-2 rounded w-full focus:outline-none focus:ring-2 focus:ring-blue-600 ${className}`}
    {...props}
  />
);

export default Input;