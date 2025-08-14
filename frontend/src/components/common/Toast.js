import React from 'react';

const Toast = ({ message, type = 'success', onClose }) => (
  <div className={`fixed bottom-4 right-4 p-4 rounded shadow text-white ${type === 'success' ? 'bg-green-600' : 'bg-red-600'}`}>
    {message}
    <button onClick={onClose} className="ml-4 text-white hover:text-gray-200">&times;</button>
  </div>
);

export default Toast;