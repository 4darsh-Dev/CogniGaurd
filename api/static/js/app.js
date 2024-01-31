const footer = document.querySelector('footer')
const navbar = document.querySelector('.navbar')
const contentScetion = document.querySelector('.content-section')
let flag = true
document.addEventListener('scroll', () => {
  console.log(
    window.scrollY,
    window.innerHeight,
    window.scrollY + window.innerHeight,
    footer.offsetTop
  )
  if (
    window.scrollY + window.innerHeight >= footer.offsetTop &&
    flag === true
  ) {
    navbar.style.position = 'absolute'
    navbar.style.top = footer.offsetTop - navbar.scrollHeight - 50 + 'px'
    flag = false
  } else if (
    flag === false &&
    window.scrollY + window.innerHeight < footer.offsetTop
  ) {
    navbar.style.position = 'fixed'
    navbar.style.top = null
    flag = true
  }
})
//  scrllY + innerHeight = offsetHeight
