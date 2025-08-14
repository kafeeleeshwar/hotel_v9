import React from 'react';
import LoginForm from '../components/forms/LoginForm';

const Login = () => (
  <div className="max-w-7xl mx-auto px-4 py-8">
    <h1 className="text-2xl font-bold text-center">Login</h1>
    <div className="max-w-md mx-auto mt-4">
      <LoginForm />
    </div>
  </div>
);

export default Login;