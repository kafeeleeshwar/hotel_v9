import React from 'react';
import SearchForm from '../components/forms/SearchForm';

const Home = () => (
  <div className="max-w-7xl mx-auto px-4 py-8">
    <h1 className="text-3xl font-bold text-center">Welcome to LuxStay AI</h1>
    <p className="text-center text-gray-600 mt-2">Find your perfect luxury hotel with AI-powered recommendations.</p>
    <div className="mt-8">
      <SearchForm />
    </div>
  </div>
);

export default Home;