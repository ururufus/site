document.addEventListener('DOMContentLoaded', () => {
    const heart = document.querySelector('.heart-outline');

    if (!heart) return;

    const startAnimation = () => {
    heart.classList.add('animate');
  };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Запускаем анимацию, добавляя класс
                startAnimation();
                // Отключаем наблюдение, чтобы не перезапускать
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.3, // Сработает, когда 30% элемента видно
        rootMargin: '0px 0px -100px 0px' // Небольшой запас снизу
    });

    const isSafari = () => {
        const ua = navigator.userAgent;
        // Safari имеет WebKit, но не Chrome, не iOS WebView, не сторонние браузеры
        return /Safari/.test(ua) &&
            /Apple Computer/.test(navigator.vendor) &&
            !/Chrome|CriOS|FxiOS|EdgiOS|OPR/.test(ua);
    };

    // Использование:
    if (isSafari()) {
        setTimeout(startAnimation, 5000);
    } else {
        observer.observe(heart);
    }
});
