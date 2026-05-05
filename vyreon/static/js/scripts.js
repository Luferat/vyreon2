// vyreon\static\js\scripts.js

const navbarCollapse = document.getElementById('mynavbar');
const bsCollapse = new bootstrap.Collapse(navbarCollapse, { toggle: false });

window.addEventListener('resize', () => {
    bsCollapse.hide();
});