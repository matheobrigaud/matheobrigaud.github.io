/* =====================================================
   Portfolio JavaScript
   =====================================================

   Ce fichier gère 4 comportements :

   1. NAVBAR au scroll
      → Ajoute la classe 'scrolled' à la navbar quand
        on scrolle, ce qui change son fond.

   2. ANIMATION au chargement (Hero)
      → Ajoute 'animate-in' au hero pour déclencher
        les transitions CSS (opacity + translateY).

   3. BARRES DE COMPÉTENCES (Intersection Observer)
      → Quand une barre est visible dans le viewport,
        on anime sa largeur de 0 → data-level%.
        L'Intersection Observer évite de charger tout
        dès le départ.

   4. TIMELINE au scroll (Intersection Observer)
      → Ajoute 'visible' aux items de la timeline
        quand ils entrent dans le viewport.

   5. MENU MOBILE
      → Toggle du menu hamburger sur mobile.

   ===================================================== */

document.addEventListener('DOMContentLoaded', () => {

  /* ------------------------------------------------
     1. NAVBAR - fond au scroll
     ------------------------------------------------ */
  const nav = document.querySelector('nav');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  });


  /* ------------------------------------------------
     2. ANIMATION HERO au chargement
     ------------------------------------------------
     Après 100ms, on ajoute 'animate-in' au hero.
     Les éléments enfants ont des 'transition-delay'
     CSS différents → effet de cascade.
  ------------------------------------------------- */
  setTimeout(() => {
    const hero = document.querySelector('.hero-inner');
    if (hero) hero.classList.add('animate-in');
  }, 100);


  /* ------------------------------------------------
     3. BARRES DE COMPÉTENCES - Intersection Observer
     ------------------------------------------------
     L'Intersection Observer déclenche une fonction
     quand un élément entre dans la zone visible.

     "threshold: 0.2" = l'élément doit être visible
     à 20% avant de déclencher l'animation.
  ------------------------------------------------- */
  const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // On récupère le niveau depuis l'attribut HTML data-level
        const fill = entry.target.querySelector('.skill-bar-fill');
        if (fill) {
          const level = fill.getAttribute('data-level');
          // Petit délai pour laisser le DOM se stabiliser
          setTimeout(() => {
            fill.style.width = level + '%';
          }, 100);
        }
        // On arrête d'observer cet élément (animation une seule fois)
        skillObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });

  // On observe chaque élément .skill-item
  document.querySelectorAll('.skill-item').forEach(el => {
    skillObserver.observe(el);
  });


  /* ------------------------------------------------
     4. TIMELINE - animation au scroll
     ------------------------------------------------
     Même principe : un Observer ajoute 'visible'
     aux éléments de la timeline quand ils entrent
     dans le viewport. Le CSS gère l'animation.
  ------------------------------------------------- */
  const timelineObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        // Délai progressif pour un effet cascading
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, i * 150);
        timelineObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.timeline-item').forEach(el => {
    timelineObserver.observe(el);
  });


  /* ------------------------------------------------
     5. MENU MOBILE - hamburger toggle
     ------------------------------------------------ */
  const toggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (toggle && navLinks) {
    toggle.addEventListener('click', () => {
      navLinks.classList.toggle('open');
    });

    // Ferme le menu au clic sur un lien
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
      });
    });
  }

});
