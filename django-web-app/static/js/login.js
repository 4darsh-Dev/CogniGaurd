let submit = document.getElementById('login-btn');

submit.addEventListener('click', function(event){
    let myForm = document.getElementById('my-form');

    // prevent defualt submission
    event.preventDefault()

    myForm.submit();
    console.log('Submitted Successfully! ');
    
})

let input = document.getElementById('password');

input.addEventListener("keypress", function(event){
    if (event.key==="Enter"){
        // prevents the defualt options.
        event.preventDefault();

        //click the button.
        document.getElementById("login-btn").click();

    }

})

// For Error message displaying and closing it 
let crossBtn = document.getElementById("cross-btn");
let errorMsgElem = document.getElementById("error-message");

crossBtn.addEventListener("click", function(){
    errorMsgElem.style.display = "none";

})

document.addEventListener("DOMContentLoaded", function(){

    // Setting timeout for n Seconds
    setTimeout(() => {
        if(errorMsgElem){
            errorMsgElem.style.display = "none";
        }
    }, 5000); 

    
})


// show password
function togglePasswordVisibility() {
    const passwordField = document.getElementById('password');
    const toggleIcon = document.getElementById('togglePassword');
    const isPasswordVisible = passwordField.type === 'password';
    passwordField.type = isPasswordVisible ? 'text' : 'password';
    toggleIcon.textContent = isPasswordVisible ? '🙈' : '👁️';
}
