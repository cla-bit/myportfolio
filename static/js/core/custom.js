const puffInCenterElements = document.querySelectorAll('.puff-in-center');
puffInCenterElements.forEach((element, index) => {
    element.style.animationDelay = index * 0.2 + 's';  /* Adjust delay as needed */
});
