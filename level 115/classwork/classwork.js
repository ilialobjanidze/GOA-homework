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

  return (
    <div >
      <h1> Student Grade Tracker</h1>

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
        <button
          onClick={addStudent}
        >
          Add
        </button>
      </div>

      {/* Threshold Input */}
      <div>
        <label >Threshold:</label>
        <input
          type="number"
          value={threshold}
          onChange={(e) => setThreshold(Number(e.target.value))}
        />
      </div>

      {/* Student Table */}
      <table >
        <thead>
          <tr>
            <th>Name</th>
            <th>Grade</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {students.map((student) => {
            const isAbove = student.grade >= threshold;
            return (
              <tr
                key={student.id}
              >
                <td>{student.name}</td>
                <td>{student.grade}</td>
                <td>
                  <button
                    onClick={() => deleteStudent(student.id)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>

      
      <div>
        <strong>Average Grade:</strong> {averageGrade()}
      </div>
    </div>
  );
}
