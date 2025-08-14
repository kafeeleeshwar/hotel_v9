import React from 'react';
import { Link } from 'react-router-dom';

const Footer = () => (
  <footer className="bg-gray-800 text-white py-6">
    <div className="max-w-7xl mx-auto px-4 text-center">
      <p>&copy; 2025 LuxStay AI. All rights reserved.</p>
      <div className="mt-2">
        <Link to="/about" className="px-2 hover:underline">About</Link>
        <Link to="/contact" className="px-2 hover:underline">Contact</Link>
        <Link to="/privacy" className="px-2 hover:underline">Privacy Policy</Link>
      </div>
    </div>
  </footer>
);

export default Footer;