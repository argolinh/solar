document.addEventListener('DOMContentLoaded', () => {
    let currentIndex = 0;
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;

    function showNextSlide() {
        slides[currentIndex].classList.remove('current-slide');
        currentIndex = (currentIndex + 1) % totalSlides;
        slides[currentIndex].classList.add('current-slide');
    }

    // Mostrar o primeiro slide
    slides[currentIndex].classList.add('current-slide');

    // Configurar intervalo para trocar os slides
    setInterval(showNextSlide, 5000);
});
