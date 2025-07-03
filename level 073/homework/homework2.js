const img = document.getElementById("img");
const next = document.getElementById("next");
const prev = document.getElementById("prev");
let i = 0;

const images = [
  "/level 73/homework/images/1.jpg",
  "/level 73/homework/images/2.jpg",
  "/level 73/homework/images/3.jpg",
  "/level 73/homework/images/4.jpg",
  "/level 73/homework/images/5.jpg",
  "/level 73/homework/images/6.jpg"

];

next.addEventListener("click", () => {
  i++;
  if (i == images.length) {
    i = 0;
  }
  img.src = images[i];
});

prev.addEventListener("click", () => {
  i--;
  if (i == -1) {
    i = images.length - 1;
  }
  img.src = images[i];
});
