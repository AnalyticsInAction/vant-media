const lightbox = document.querySelector('#lightbox');
const lightboxImage = document.querySelector('#lightbox-image');
let lastTrigger;
document.querySelectorAll('[data-image]').forEach(button => {
  button.addEventListener('click', () => {
    lastTrigger = button;
    lightboxImage.src = button.dataset.image;
    lightboxImage.alt = button.querySelector('img').alt;
    document.querySelector('#lightbox-title').textContent = button.dataset.title;
    lightbox.showModal();
    document.body.style.overflow = 'hidden';
  });
});
document.querySelector('.close').addEventListener('click', () => lightbox.close());
lightbox.addEventListener('click', event => { if (event.target === lightbox) lightbox.close(); });
lightbox.addEventListener('close', () => { document.body.style.overflow = ''; lastTrigger?.focus(); });
document.querySelector('#year').textContent = new Date().getFullYear();
