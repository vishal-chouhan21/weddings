// Close button handler (Ganesh card)
document.addEventListener('DOMContentLoaded', function () {
  const closeBtn = document.querySelector('.close-btn');
  if (closeBtn) {
    closeBtn.addEventListener('click', function () {
      window.history.back();
    });
  }
});
