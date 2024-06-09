// messages.js

document.addEventListener('DOMContentLoaded', function() {
    // Add click event listener to close buttons
    document.querySelectorAll('.message .close').forEach(function(closeButton) {
        closeButton.addEventListener('click', function() {
            var message = this.parentElement;
            message.style.opacity = '0';
            setTimeout(function() {
                message.style.display = 'none';
            }, 500);
        });
    });

    // Automatically hide messages after 5 seconds
    setTimeout(function() {
        document.querySelectorAll('.message').forEach(function(message) {
            message.style.opacity = '0';
            setTimeout(function() {
                message.style.display = 'none';
            }, 500);
        });
    }, 5000);
});
