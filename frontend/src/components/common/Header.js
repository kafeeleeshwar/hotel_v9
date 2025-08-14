import React, { useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { AuthContext } from '../../context/AuthContext';

const Header = () => {
  const { user, logout } = useContext(AuthContext);
  const navigate = useNavigate();

  return (
    <header className="bg-white shadow">
      <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold text-blue-600">LuxStay AI</Link>
        <nav>
          <Link to="/hotels" className="px-4 py-2 text-blue-600 hover:text-blue-800">Hotels</Link>
          {user ? (
            <>
              <Link to="/profile" className="px-4 py-2 text-blue-600 hover:text-blue-800">Profile</Link>
              <Link to="/my-bookings" className="px-4 py-2 text-blue-600 hover:text-blue-800">My Bookings</Link>
              <button onClick={() => { logout(); navigate('/'); }} className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700">Logout</button>
            </>
          ) : (
            <>
              <Link to="/login" className="px-4 py-2 text-blue-600 hover:text-blue-800">Login</Link>
              <Link to="/register" className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">Register</Link>
            </>
          )}
        </nav>
      </div>
    </header>
  );
};

export default Header;