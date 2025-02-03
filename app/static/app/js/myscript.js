document.addEventListener("DOMContentLoaded", function () {
    const plusButtons = document.querySelectorAll(".plus-cart");
    const minusButtons = document.querySelectorAll(".minus-cart");

    // Handle quantity increment
    plusButtons.forEach(button => {
        button.addEventListener("click", function () {
            const pid = this.getAttribute("pid");
            const quantityElement = document.querySelector(`.quantity[data-pid="${pid}"]`);

            if (!quantityElement) return;

            let currentQuantity = parseInt(quantityElement.textContent);
            updateQuantity(pid, currentQuantity + 1);
        });
    });

    // Handle quantity decrement
    minusButtons.forEach(button => {
        button.addEventListener("click", function () {
            const pid = this.getAttribute("pid");
            const quantityElement = document.querySelector(`.quantity[data-pid="${pid}"]`);

            if (!quantityElement) return;

            let currentQuantity = parseInt(quantityElement.textContent);
            if (currentQuantity > 1) {
                updateQuantity(pid, currentQuantity - 1);
            }
        });
    });

    // Function to update quantity via AJAX
    function updateQuantity(pid, newQuantity) {
        fetch('/update-cart/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
            body: JSON.stringify({ pid: pid, quantity: newQuantity }),
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Update the quantity in the UI
                    const quantityElement = document.querySelector(`.quantity[data-pid="${pid}"]`);
                    if (quantityElement) {
                        quantityElement.textContent = data.new_quantity;
                    }

                    // Update total amounts
                    document.getElementById("amount").textContent = `Rs.${data.total_amount.toFixed(2)}`;
                    document.getElementById("totalamount").textContent = `Rs.${data.total_with_shipping.toFixed(2)}`;
                } else {
                    console.error(data.error || 'Failed to update quantity');
                }
            })
            .catch(error => console.error('Error:', error));
    }

    // Get CSRF token for Django
    function getCSRFToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
    }
});
