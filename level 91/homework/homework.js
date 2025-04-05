const searchBtn = document.querySelector(".search-btn");
const searchInput = document.querySelector("#search");
const resultsDiv = document.querySelector("#results");

function fetchBooks() {
    const query = searchInput.value.trim();
    if (!query) return;
    fetch(`https://www.googleapis.com/books/v1/volumes?q=${query}`)
        .then(res => res.json())
        .then(data => {
            resultsDiv.innerHTML = data.items?.map(({ volumeInfo: b }) => `
                <div class='book'>
                    <img src="${b.imageLinks?.thumbnail || ''}" alt="${b.title}">
                    <h3>${b.title}</h3>
                    <p>Release Date: ${b.publishedDate || 'Unknow'}</p>
                    <p>Pages: ${b.pageCount || 'Unknow'}</p>
                    <p>${b.description ? b.description.slice(0, 100) + '...' : 'No Description'}</p>
                </div>
            `).join('');
        });
}

searchBtn.addEventListener("click", fetchBooks);