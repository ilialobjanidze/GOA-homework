import React, { useState } from 'react';

// სტუდენტის ბარათი
const StudentCard = ({ name, grade }) => {
  return (
    <div style={styles.card}>
      <h3>{name}</h3>
      <p>Grade: {grade}</p>
    </div>
  );
};

const App = () => {
  const [students, setStudents] = useState([
    { name: 'Ilia', grade: 85 },
    { name: 'Nino', grade: 92 },
    { name: 'David', grade: 78 },
    { name: 'Ana', grade: 95 },
    { name: 'Giorgi', grade: 88 },
  ]);

  const sortAscending = () => {
    const sorted = [...students].sort((a, b) => a.grade - b.grade);
    setStudents(sorted);
  };

  const sortDescending = () => {
    const sorted = [...students].sort((a, b) => b.grade - a.grade);
    setStudents(sorted);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Student Grades</h1>

      <div style={{ marginBottom: '15px' }}>
        <button onClick={sortAscending} style={styles.button}>Sort Ascending</button>
        <button onClick={sortDescending} style={{ ...styles.button, marginLeft: 10 }}>Sort Descending</button>
      </div>

      <div style={styles.grid}>
        {students.map((student, index) => (
          <StudentCard key={index} {...student} />
        ))}
      </div>
    </div>
  );
};

const styles = {
  grid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
    gap: '15px',
  },
  card: {
    border: '1px solid #ccc',
    borderRadius: '10px',
    padding: '15px',
    textAlign: 'center',
    boxShadow: '0 0 8px rgba(0,0,0,0.1)',
    backgroundColor: '#fff',
  },
  button: {
    padding: '10px 15px',
    fontSize: '16px',
    cursor: 'pointer',
    borderRadius: '5px',
    border: 'none',
    backgroundColor: '#007bff',
    color: 'white',
  },
};

export default App;
