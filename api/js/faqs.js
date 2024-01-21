const faqs = document.querySelectorAll('.faq')
faqs.forEach((faq) => {
  const button = faq.querySelector('.faq-button')
  const faqContent = faq.querySelector('.faq-answer')
  button.addEventListener('click', () => {
    button.classList.toggle('rotate')
    faqContent.classList.toggle('show')
  })
})
