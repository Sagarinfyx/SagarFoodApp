document.addEventListener("DOMContentLoaded", function () {
    const quantityInput = document.querySelector(".quantity");
    const decrementButton = document.querySelector(".decrement");
    const incrementButton = document.querySelector(".increment");
    const cartQuantityInput = document.querySelector(".cart-quantity");
  
    decrementButton.addEventListener("click", () => {
      let quantity = parseInt(quantityInput.value);
      if (quantity > 1) {
        quantityInput.value = quantity - 1;
        cartQuantityInput.value = quantity - 1;
      }
    });
  
    incrementButton.addEventListener("click", () => {
      let quantity = parseInt(quantityInput.value);
      quantityInput.value = quantity + 1;
      cartQuantityInput.value = quantity + 1;
    });
  });
  