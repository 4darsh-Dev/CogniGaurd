const faqs = document.querySelectorAll('.faq')
faqs.forEach((faq) => {
  const button = faq.querySelector('.faq-button')
  const faqContent = faq.querySelector('.faq-answer')
  button.addEventListener('click', () => {
    button.classList.toggle('rotate')
    if (faqContent.style.maxHeight) {
      faqContent.style.maxHeight = null
    } else {
      faqContent.style.maxHeight = faqContent.scrollHeight + 'px'
    }

    faqContent.classList.toggle('show')
  })
})
