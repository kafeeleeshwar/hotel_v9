import React from 'react';
import { Link } from 'react-router-dom';

const NotFound = () => (
  <div className="max-w-7xl mx-auto px-4 py-8 text-center">
    <h1 className="text-3xl font-bold">404 - Page Not Found</h1>
    <p className="mt-4">The page you're looking for doesn't exist.</p>
    <Link to="/" className="mt-4 inline-block text-blue-600 hover:underline">Go to Home</Link>
  </div>
);

export default NotFound;