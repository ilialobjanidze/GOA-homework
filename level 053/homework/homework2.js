const image = document.getElementById('image');
const changeSrcButton = document.getElementById('changeSrcButton');

changeSrcButton.addEventListener('click', () => {
    image.src = 'example2.jpg';
});
