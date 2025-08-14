import React from 'react';

const Badge = ({ children, className = '' }) => (
  <span className={`px-2 py-1 bg-blue-100 text-blue-800 text-sm rounded ${className}`}>
    {children}
  </span>
);

export default Badge;