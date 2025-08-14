export const formatDate = (date) => {
  return new Date(date).toLocaleDateString();
};

export const formatPrice = (price) => {
  return `$${parseFloat(price).toFixed(2)}`;
};