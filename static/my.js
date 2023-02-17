function toggleNavbarOpacity() {
  // Get the navbar element
  var navbar = document.getElementById("navbar");

  // Get the current scroll position
  var scrollPos = window.scrollY;

  // If the user has scrolled past the navbar height, add the "scrolled" class
  if (scrollPos > navbar.offsetHeight) {
    navbar.classList.add("scrolled");
  }
  // Otherwise, remove the "scrolled" class
  else {
    navbar.classList.remove("scrolled");
  }
}

// Add an event listener to the window to listen for scroll events
window.addEventListener("scroll", toggleNavbarOpacity);

//========= Category Slider (tiny slider library)
tns({
  container: ".recentPostSlider",
  items: 3,
  slideBy: "page",
  autoplay: false,
  mouseDrag: true,
  gutter: 0,
  nav: false,
  controls: true,
  controlsText: [
    '<i class="fas fa-chevron-left"></i>',
    '<i class="fas fa-chevron-right"></i>',
  ],
  responsive: {
    0: {
      items: 1,
    },
    540: {
      items: 2,
    },
    768: {
      items: 3,
    },
    992: {
      items: 4,
    },
    1170: {
      items: 5,
    },
  },
});


const typedTextSpan = document.querySelector(".typed-text");
const cursorSpan = document.querySelector(".cursor");

const textArray = ["ROOM", "LIFE", "ROOMIE", "TENANTS"];
const typingDelay = 200;
const erasingDelay = 100;
const newTextDelay = 2000; // Delay between current and next text
let textArrayIndex = 0;
let charIndex = 0;

function type() {
  if (charIndex < textArray[textArrayIndex].length) {
    if(!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
    typedTextSpan.textContent += textArray[textArrayIndex].charAt(charIndex);
    charIndex++;
    setTimeout(type, typingDelay);
  } 
  else {
    cursorSpan.classList.remove("typing");
  	setTimeout(erase, newTextDelay);
  }
}

function erase() {
	if (charIndex > 0) {
    if(!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
    typedTextSpan.textContent = textArray[textArrayIndex].substring(0, charIndex-1);
    charIndex--;
    setTimeout(erase, erasingDelay);
  } 
  else {
    cursorSpan.classList.remove("typing");
    textArrayIndex++;
    if(textArrayIndex>=textArray.length) textArrayIndex=0;
    setTimeout(type, typingDelay + 1100);
  }
}

document.addEventListener("DOMContentLoaded", function() { // On DOM Load initiate the effect
  if(textArray.length) setTimeout(type, newTextDelay + 250);
});