import React, { useState } from 'react';

export default function StudentGradeTracker() {
  const [students, setStudents] = useState([]);
  const [name, setName] = useState('');
  const [grade, setGrade] = useState('');
  const [threshold, setThreshold] = useState(75);

  const addStudent = () => {
    if (!name || isNaN(grade)) return;
    const newStudent = {
      id: Date.now(),
      name,
      grade: Number(grade),
    };
    setStudents([...students, newStudent]);
    setName('');
    setGrade('');
  };

  const deleteStudent = (id) => {
    setStudents(students.filter((s) => s.id !== id));
  };

  const averageGrade = () => {
    if (students.length === 0) return 0;
    const total = students.reduce((sum, s) => sum + s.grade, 0);
    return (total / students.length).toFixed(2);
  };

  const sortAscending = () => {
    const sorted = [...students].sort((a, b) => a.grade - b.grade);
    setStudents(sorted);
  };

  const sortDescending = () => {
    const sorted = [...students].sort((a, b) => b.grade - a.grade);
    setStudents(sorted);
  };

  return (
    <div>
      <h1>Student Grade Tracker</h1>

      {/* Add Student Form */}
      <div>
        <input
          type="text"
          placeholder="Student Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="number"
          placeholder="Grade"
          value={grade}
          onChange={(e) => setGrade(e.target.value)}
        />
        <button onClick={addStudent}>Add</button>
      </div>

      {/* Threshold Input */}
      <div>
        <label>Threshold:</label>
        <input
          type="number"
          value={threshold}
          onChange={(e) => setThreshold(Number(e.target.value))}
        />
      </div>

      <div style={{ marginTop: '10px' }}>
        <button onClick={sortAscending}>Sort by Grade ↑</button>
        <button onClick={sortDescending} style={{ marginLeft: '10px' }}>
          Sort by Grade ↓
        </button>
      </div>

      <table style={{ marginTop: '10px', borderCollapse: 'collapse', width: '100%' }}>
        <thead>
          <tr>
            <th style={{ border: '1px solid #ddd', padding: '8px' }}>Name</th>
            <th style={{ border: '1px solid #ddd', padding: '8px' }}>Grade</th>
            <th style={{ border: '1px solid #ddd', padding: '8px' }}>Action</th>
          </tr>
        </thead>
        <tbody>
          {students.map((student) => {
            const isAbove = student.grade >= threshold;
            return (
              <tr key={student.id}>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{student.name}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{student.grade}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>
                  <button onClick={() => deleteStudent(student.id)}>Delete</button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>

      <div style={{ marginTop: '10px' }}>
        <strong>Average Grade:</strong> {averageGrade()}
      </div>
    </div>
  );
}
