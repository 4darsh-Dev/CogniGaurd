document.addEventListener('DOMContentLoaded', (event) => {
    // Smooth scroll to anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Add 'back to top' button functionality
    const backToTopButton = document.createElement('button');
    backToTopButton.innerHTML = '<i class="fa-solid fa-arrow-up"></i>';
    backToTopButton.setAttribute('id', 'backToTop');
    backToTopButton.style.display = 'none';
    document.body.appendChild(backToTopButton);

    window.onscroll = function() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    };

    backToTopButton.addEventListener('click', function(){
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    });
});
