// footer js
document.addEventListener('DOMContentLoaded', function () {
    const ctaButton = document.querySelector('.cta-button-footer');

    ctaButton.addEventListener('mouseover', function () {
        this.style.transform = 'scale(1.05)';
    });

    ctaButton.addEventListener('mouseout', function () {
        this.style.transform = 'scale(1)';
    });
});


