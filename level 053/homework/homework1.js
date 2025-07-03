const image = document.getElementById('image');
const resizeButton = document.getElementById('resizeButton');

resizeButton.addEventListener('click', () => {
    image.style.width = '400px';
    image.style.height = '300px';
});
