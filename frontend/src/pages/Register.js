import React from 'react';
import RegisterForm from '../components/forms/RegisterForm';

const Register = () => (
  <div className="max-w-7xl mx-auto px-4 py-8">
    <h1 className="text-2xl font-bold text-center">Register</h1>
    <div className="max-w-md mx-auto mt-4">
      <RegisterForm />
    </div>
  </div>
);

export default Register;