window.onload = () => {
  const submitBtn = document.getElementById("submit");
  const username = document.getElementById("username");
  submitBtn.addEventListener("click", (e) => {
    console.log(username.checkValidity())
    e.preventDefault();
    if (username.value && username.checkValidity()) {
      window.location.href = `/user/${username.value}`;
    } else {
      document.getElementById('validation').innerText = username.validationMessage 
    }
  });
};
