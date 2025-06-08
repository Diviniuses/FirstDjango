function showItemDetails(name, quantity) {
    document.getElementById('modalTitle').textContent = name;
    document.getElementById('modalQuantity').textContent = 'Количество: ' + quantity;
    document.getElementById('itemModal').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
}

function closeModal() {
    document.getElementById('itemModal').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function() {
    const overlay = document.getElementById('overlay');
    if (overlay) {
        overlay.onclick = closeModal;
    }
}); 