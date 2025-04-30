
let contactWrapperElement = null;
let formWrapperElement = null;

function moveIn() {
    const textElement = contactWrapperElement.querySelector('.text');
    if (textElement)
        textElement.after(formWrapperElement);
}

function moveOut() {
    contactWrapperElement.after(formWrapperElement);
}

function move() {
    if (window.innerWidth <= 500)
        moveIn();
    else
        moveOut();
}

function init() {
    contactWrapperElement = document.querySelector('.contact-infos-wrapper');
    formWrapperElement = document.querySelector('.form-wrapper');

    if (window.innerWidth <= 500)
        moveIn();

    // Attach resize event
    window.addEventListener('resize', move);
}

// Run on page load
document.addEventListener('DOMContentLoaded', init);