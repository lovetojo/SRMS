const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

function isValidMatricNumber(matricNumber) {
    // Implement your matric number validation logic
    const matricNumberRegex = /^\d{2}\/[A-Z]{3}\d{2}\/\d{3}$/;
    return matricNumberRegex.test(matricNumber);
}

function isValidPassword(password) {
    // Implement your password validation logic
    const passwordRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return passwordRegex.test(password);
}

function checkSignIn() {
    const matricNumber = document.getElementById('matricNumberSignIn').value;
    const password = document.getElementById('passwordSignIn').value;

    const matricNumberIsValid = isValidMatricNumber(matricNumber);
    const passwordIsValid = isValidPassword(password);

    // Implement logic to display ticks or messages based on validity
    // For simplicity, we'll log the results to the console
    console.log("Matric Number Valid:", matricNumberIsValid);
    console.log("Password Valid:", passwordIsValid);
}

function checkSignUp() {
    // Similar to checkSignIn, implement the logic for sign-up form
}
