import React, { useState } from 'react';

const MovieCard = ({ title, image, description, rating, genre, releaseDate }) => {
  const [showMore, setShowMore] = useState(false);

  return (
    <div style={styles.card}>
      <img src={image} alt={title} style={styles.image} />
      <h2>{title}</h2>
      <p>{description}</p>

      {showMore && (
        <div style={styles.details}>
          <p><strong>Rating:</strong> {rating}</p>
          <p><strong>Genre:</strong> {genre}</p>
          <p><strong>Release Date:</strong> {releaseDate}</p>
        </div>
      )}

      <button onClick={() => setShowMore(!showMore)} style={styles.button}>
        {showMore ? 'Hide Info' : 'More Info'}
      </button>
    </div>
  );
};

const styles = {
  card: {
    border: '1px solid #ccc',
    borderRadius: '12px',
    padding: '15px',
    textAlign: 'center',
    boxShadow: '0 0 10px rgba(0,0,0,0.1)',
    backgroundColor: '#fff'
  },
  image: {
    width: '100%',
    height: '300px',
    objectFit: 'cover',
    borderRadius: '8px'
  },
  details: {
    marginTop: '10px',
    textAlign: 'left'
  },
  button: {
    marginTop: '10px',
    padding: '8px 12px',
    border: 'none',
    backgroundColor: '#007bff',
    color: 'white',
    borderRadius: '5px',
    cursor: 'pointer'
  }
};

export default MovieCard;
