const OWNER = 'Team CogniGuard';
console.log(`Author: ${OWNER}`);

document.addEventListener('DOMContentLoaded', function() {
    const dropdown = document.querySelector('.dropdown');
    const dropdownMenu = document.querySelector('.dropdown-menu');

    // Add a small delay when moving from dropdown toggle to menu
    let timeoutId;

    dropdown.addEventListener('mouseenter', function() {
        clearTimeout(timeoutId);
        dropdownMenu.style.display = 'block';
    });

    dropdown.addEventListener('mouseleave', function() {
        timeoutId = setTimeout(() => {
            dropdownMenu.style.display = 'none';
        }, 100); // 100ms delay
    });

    dropdownMenu.addEventListener('mouseenter', function() {
        clearTimeout(timeoutId);
    });

    dropdownMenu.addEventListener('mouseleave', function() {
        dropdownMenu.style.display = 'none';
    });
});


document.addEventListener('DOMContentLoaded', () => {
    const section = document.querySelector('.elastic-section');
    const title = section.querySelector('.title');
    const description = section.querySelector('.description');
    const ctaContainer = section.querySelector('.cta-container');
  
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          title.style.animation = 'fadeInUp 0.8s ease forwards';
          description.style.animation = 'fadeInUp 0.8s ease forwards 0.2s';
          ctaContainer.style.animation = 'fadeInUp 0.8s ease forwards 0.4s';
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
  
    observer.observe(section);
  });


// Scalabilty section js

document.addEventListener('DOMContentLoaded', () => {
    const visual = document.querySelector('.visual');
    const servers = document.querySelectorAll('.server');
    const particles = document.querySelectorAll('.particle');
    const hexagon = document.querySelector('.hexagon');
  
    // Animate servers
    servers.forEach((server, index) => {
      server.style.animation = `float ${3 + index * 0.5}s ease-in-out infinite`;
    });
  
    // Animate particles
    particles.forEach((particle, index) => {
      particle.style.animation = `orbit ${5 + index * 2}s linear infinite`;
    });
  
    // Animate hexagon
    hexagon.style.animation = 'pulse 4s ease-in-out infinite';
  
    // Create 3D effect on hover
    visual.addEventListener('mousemove', (e) => {
      const { left, top, width, height } = visual.getBoundingClientRect();
      const x = (e.clientX - left) / width;
      const y = (e.clientY - top) / height;
  
      const tiltX = (y - 0.5) * 20;
      const tiltY = (x - 0.5) * 20;
  
      visual.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg)`;
    });
  
    visual.addEventListener('mouseleave', () => {
      visual.style.transform = 'perspective(1000px) rotateX(0) rotateY(0)';
    });
  
    // Add parallax effect
    document.addEventListener('mousemove', (e) => {
      const mouseX = e.clientX / window.innerWidth;
      const mouseY = e.clientY / window.innerHeight;
  
      servers.forEach((server, index) => {
        const depth = 1 + index * 0.1;
        const translateX = (mouseX - 0.5) * 50 * depth;
        const translateY = (mouseY - 0.5) * 50 * depth;
        server.style.transform = `translate(${translateX}px, ${translateY}px)`;
      });
  
      particles.forEach((particle, index) => {
        const depth = 1 + index * 0.2;
        const translateX = (mouseX - 0.5) * 30 * depth;
        const translateY = (mouseY - 0.5) * 30 * depth;
        particle.style.transform = `translate(${translateX}px, ${translateY}px)`;
      });
    });
  });

// flexibilty section js
document.addEventListener('DOMContentLoaded', function () {
    const shapes = document.querySelectorAll('.animated-shapes i');

    shapes.forEach(shape => {
        const moveShape = () => {
            const x = Math.random() * window.innerWidth;
            const y = Math.random() * window.innerHeight;
            shape.style.transform = `translate(${x}px, ${y}px)`;
        };

        setInterval(moveShape, 5000);
    });
});

// esre section js
// document.addEventListener('DOMContentLoaded', function() {
//   const shapesContainer = document.getElementById('animated-shapes');

//   // Create shapes
//   for (let i = 0; i < 4; i++) {
//       const shape = document.createElement('div');
//       shape.classList.add('shape-esre');
//       shapesContainer.appendChild(shape);
//   }
// });


// Hamburger menu button changes
let menuBtnCond = true;
let checkLabel = document.getElementById("check-label");

const menuBtnChanger = function(){

    if (menuBtnCond){
        checkLabel.innerHTML = `<i class="fas fa-times close-icon"></i>`;
        menuBtnCond = false;
    }

    else{
        checkLabel.innerHTML = `<i class="fas fa-bars menu-icon"></i>`;

        menuBtnCond = true;
    }

}

let menuBtn = document.getElementById("check");
menuBtn.addEventListener("click", menuBtnChanger);





// back to top button js


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
  backToTopButton.innerHTML = `<i class="fa-solid fa-arrow-up"></i>`;
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