const faqs = document.querySelectorAll('.faq')
faqs.forEach((faq) => {
  const button = faq.querySelector('.faq-button')
  const faqContent = faq.querySelector('.faq-answer')
  button.addEventListener('click', () => {
    button.classList.toggle('rotate')
    if (faqContent.style.maxHeight) {
      faqContent.style.maxHeight = null
    } else {
      faqContent.style.maxHeight = faqContent.scrollHeight + 100 + 'px'
    }
    if (faqContent.classList.contains('show')) {
      setTimeout(() => {
        faqContent.classList.remove('show')
      }, 250)
    } else {
      faqContent.classList.add('show')
    }
  })
})
