import React from 'react';
import MovieCard from './MovieCard';

const App = () => {
  const movies = [
    {
      title: 'Inception',
      image: 'https://m.media-amazon.com/images/I/51s+H8hIqUL._AC_.jpg',
      description: 'A thief who steals corporate secrets through dream-sharing.',
      rating: '8.8',
      genre: 'Sci-Fi',
      releaseDate: '2010'
    },
    {
      title: 'The Dark Knight',
      image: 'https://m.media-amazon.com/images/I/51K8ouYrHeL._AC_.jpg',
      description: 'Batman faces the Joker, a criminal mastermind.',
      rating: '9.0',
      genre: 'Action',
      releaseDate: '2008'
    },
    {
      title: 'Interstellar',
      image: 'https://m.media-amazon.com/images/I/81tEgsxpNZS._AC_SL1500_.jpg',
      description: 'A team travels through a wormhole to save humanity.',
      rating: '8.6',
      genre: 'Adventure',
      releaseDate: '2014'
    }
  ];

  return (
    <div style={styles.gallery}>
      {movies.map((movie, index) => (
        <MovieCard key={index} {...movie} />
      ))}
    </div>
  );
};

const styles = {
  gallery: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
    gap: '20px',
    padding: '20px'
  }
};

export default App;
