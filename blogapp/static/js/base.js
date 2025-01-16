document
  .querySelector(".navbar-nav li:last-child")
  .addEventListener("click", () => {
    document.querySelector("#logoutForm").submit();
  });
