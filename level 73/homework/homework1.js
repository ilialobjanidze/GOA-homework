const img = document.getElementById("img");
const next = document.getElementById("next");
const prev = document.getElementById("prev");
let i = 0;

const images = [
  "/level 73/homework/iamges/download (1).jpg",
  "/level 73/homework/iamges/download (2).jpg",
  "/level 73/homework/iamges/download (3).jpg",
  "/level 73/homework/iamges/download (4).jpg",
  "/level 73/homework/iamges/download.jpgs"

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
