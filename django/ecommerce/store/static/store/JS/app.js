function addToCart(productId) {
    fetch(`/api/cart/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ product_id: productId })
    })
    .then(response => response.json())
    .then(data => {
        alert("Added to cart!");
    });
}