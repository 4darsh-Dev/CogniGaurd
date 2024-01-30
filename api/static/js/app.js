// function setSpeed(speed) {
//   const needle = document.getElementById('needle')
//   needle.style.transform = `rotate(${speed}deg)`
// }
// let transparencyScore = prompt('Enter transparency Score (0-100)')
// // adjusting according to transparency score
// if (transparencyScore >= 8) {
//   setSpeed(270)
// } else if (transparencyScore <= 4) {
//   setSpeed(90)
// } else {
//   setSpeed(0)
// }
// animation
const img = document.querySelector('.animate-img')
const p = document.querySelector('.animate-p')
console.log(img.getBoundingClientRect().top, img.offsetHeight)
const animate = (element) => {
  if (
    window.scrollY >
    element.getBoundingClientRect().top + element.offsetHeight
  ) {
    element.classList.add('animate')
  }
  if (
    window.scrollY <
    element.getBoundingClientRect().top + element.offsetHeight + 100
  ) {
    element.classList.remove('animate')
  }
}
const animateAll = () => {
  animate(img)
  animate(p)
}
document.addEventListener('scroll', animateAll)
