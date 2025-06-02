import React from 'react';
import { createRoot } from 'react-dom/client';

const container = document.getElementById('root');
const root = createRoot(container);

const title = "";
const background = (
  <img className="background" alt="ocean" src="/images/ocean.jpg" />
); 
const images = [];
for (const animal in animals) {
  images.push(
    <img
      key={animal}
      className="animal"
      alt={animal}
      src={animals[animal].image}
    />
  );
}
const animalFacts = (
  <div>
    {background}
    <h1>{title || 'Click an animal for a fun fact'}</h1>
    <p id="fact"></p>
    <div className="animals">{images}</div>
  </div>
);

const showBackground = true;

if (showBackground) {
  root.render(animalFacts);
} else {
  root.render(
    <div>
      <h1>{title || 'Click an animal for a fun fact'}</h1>
      <p id="fact"></p>
      <div className="animals">{images}</div>
    </div>
  );
}

function displayFact(e) {
  const animalName = e.target.alt;
  const facts = animals[animalName].facts;
  const index = Math.floor(Math.random() * facts.length);
  const fact = facts[index];
  document.getElementById('fact').innerHTML = fact;
}