const parent = document.getElementById("parent");

fetch("https://fakestoreapi.com/products")
    .then(response => response.json())
    .then(products => {
        parent.innerHTML = products.map(res => `
            <div>
                <p>Title: ${res.title}</p>
                <p>Description: ${res.description}</p>
                <p>Price: ${res.price}</p>
                <img src="${res.image}" width=200 />
            </div>
        `).join('');
    });
