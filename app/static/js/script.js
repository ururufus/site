document.addEventListener('DOMContentLoaded', () => {
    const heart = document.querySelector('.heart-outline');
    
    if (!heart) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Запускаем анимацию, добавляя класс
                heart.classList.add('animate');
                // Отключаем наблюдение, чтобы не перезапускать
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.3, // Сработает, когда 30% элемента видно
        rootMargin: '0px 0px -100px 0px' // Небольшой запас снизу
    });

    observer.observe(heart);
});