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

// menu transition
const menu = document.querySelector('.hamburger-menu ')
const sideBar = document.querySelector('.navbar__links')
const hamburgerMenu = document.querySelector('.hamburger-menu')
const overlay = document.querySelector('#overlay')

hamburgerMenu.addEventListener('click', () => {
  hamburgerMenu.classList.toggle('change')
  overlay.style.display = hamburgerMenu.classList.contains('change')
    ? 'block'
    : 'none'
  hamburgerMenu.classList.toggle('change')
})
menu.addEventListener('click', () => {
  sideBar.classList.toggle('show')
})
