let submit = document.getElementById('signup-btn');

submit.addEventListener('click', function(){
    let myForm = document.getElementById('my-form');
    myForm.submit();
    console.log('Submitted Successfully! ');
    
})

let input = document.getElementById('cnf-password');

input.addEventListener("keypress", function(event){
    if (event.key==="Enter"){
        // prevents the defualt options.
        event.preventDefault();

        //click the button.
        document.getElementById("signup-btn").click();

    }

})

// Save form data to local storage

document.addEventListener('DOMContentLoaded', function () {
    // Populate the form with stored data if available
    const username = localStorage.getItem('register_username');
    const email = localStorage.getItem('register_email');

    if (username) document.getElementById('username').value = username;
    if (email) document.getElementById('email').value = email;

    // Save form data to local storage on input change
    document.getElementById('username').addEventListener('input', function () {
        localStorage.setItem('register_username', this.value);
    });
    document.getElementById('email').addEventListener('input', function () {
        localStorage.setItem('register_email', this.value);
    });

    // Clear local storage if there are no error messages
    const error_message = document.getElementById('error-message');
    if (!error_message) {
        localStorage.removeItem('register_username');
        localStorage.removeItem('register_email');
    }
});


// show password


function togglePasswordVisibility(passwordField, toggleIcon) {
    const isPasswordVisible = passwordField.type === 'password';
    passwordField.type = isPasswordVisible ? 'text' : 'password';
    toggleIcon.textContent = isPasswordVisible ? '🙈' : '👁️';
    console.log("I am toggled!");
}

const passFieldFirst = document.getElementById('password');
const eyeIconOne = document.getElementById("eye-icon-one");
eyeIconOne.addEventListener("click", function() {
    togglePasswordVisibility(passFieldFirst, eyeIconOne);
});

const passFieldTwo = document.getElementById('cnf-password');
const eyeIconTwo = document.getElementById("eye-icon-two");
eyeIconTwo.addEventListener("click", function() {
    togglePasswordVisibility(passFieldTwo, eyeIconTwo);
});


