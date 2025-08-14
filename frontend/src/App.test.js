import { render, screen } from '@testing-library/react';
import App from './App';

test('renders LuxStay AI header', () => {
  render(<App />);
  const linkElement = screen.getByText(/LuxStay AI/i);
  expect(linkElement).toBeInTheDocument();
});