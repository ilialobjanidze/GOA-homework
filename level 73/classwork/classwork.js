const img = document.getElementById("img");
const next = document.getElementById("next");
const prev = document.getElementById("prev");
let i = 0;

const images = [
  "/level 73/classwork/img/download (1).png",
  "/level 73/classwork/img/download (2).png",
  "/level 73/classwork/img/download (3).png",
  "/level 73/classwork/img/download.png"

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
