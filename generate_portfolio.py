"""
Portfolio Generator - Mathéo Brigaud
=============================================
Fichier mis à jour avec les données du CV et corrections techniques.
"""

# ============================================================
# DONNÉES PERSONNELLES
# ============================================================

PERSONAL_INFO = {
    "name": "Mathéo Brigaud",
    "tagline": "Étudiant BUT Science des Données",
    "subtitle": "Analyse, traitement et valorisation de la DATA",
    "email": "brigaudmatheo@gmail.com", 
    "phone": "06 29 90 72 24",
    "linkedin": "https://linkedin.com/in/matheo-brigaud", # À personnaliser
    "github": "https://github.com/matheo-brigaud",      # À personnaliser
    "location": "Niort, France", 
    "photo": "images/profile.jpg",
    "about": """Étudiant en première année de BUT Science des Données à Niort, je développe une expertise solide dans le traitement et l'analyse de données. 
    Mes résultats aux tests Pix témoignent d'une grande maîtrise en programmation et en résolution de problèmes techniques (Niveau 7).
    
    Passionné par la culture, je cultive une dualité entre la rigueur scientifique et une curiosité nourrie par la philosophie, la littérature et la poésie. 
    Sportif engagé (Rugby, Musculation), je valorise l'esprit d'équipe et la persévérance.""",
}

# ============================================================
# COMPÉTENCES (Basées sur le score Pix de 706/1024)
# ============================================================

SKILLS = [
    ("Programmation (Python)", 85, "Expertise Pix niv. 7"),
    ("Résoudre des problèmes", 85, "Expertise Pix niv. 7"),
    ("Gérer des données", 75, "Expertise Pix niv. 6"),
    ("Environnement numérique", 70, "Expertise Pix niv. 6"),
    ("Anglais (Niveau C1)", 90, "Langues"),
    ("Espagnol (Niveau B2)", 75, "Langues"),
    ("Excel / SQL", 70, "Outils techniques"),
]

# ============================================================
# EXPÉRIENCES PROFESSIONNELLES
# ============================================================

EXPERIENCES = [
    {
        "poste": "Hôte de caisse",
        "entreprise": "Super U (Villebois-Lavalette)",
        "periode": "Mars 2025 - Présent",
        "description": "Encaissement des clients et conseil en caisse libre-service.", 
        "tags": ["Relation Client", "Responsabilité"],
        "logo": "images/logo/U.jpg",
    },
    {
        "poste": "Employé commercial (BAZAR / PGC)",
        "entreprise": "Super U",
        "periode": "Octobre 2023 - Février 2025",
        "description": "Mise en rayon, étiquetage, suivi des prix et merchandising.", 
        "tags": ["Organisation", "Rigueur"],
        "logo": "images/logo/U.jpg",
    },
    {
        "poste": "Extra Serveur",
        "entreprise": "Maison Lafaye (Soyaux)",
        "periode": "2023 - 2025",
        "description": "Mise en place, service client, encaissement et rangement.", 
        "tags": ["Dynamisme", "Service"],
        "logo": "images/logo/ML.jpg",
    },
]

# ============================================================
# PROJETS UNIVERSITAIRES
# ============================================================

PROJECTS = [
    {
        "titre": "Production de données en entreprise",
        "description": "Collecte et regroupement de données INSEE. Analyse et traitement de bases de données.", 
        "image": "images/projects/insee.jpg",
        "tags": ["Data Analysis", "INSEE", "Python"],
        "date": "2025",
        "featured": True,
    },
    {
        "titre": "Lieu économique et culturel",
        "description": "Présentation historique en français et analyse économique en anglais (C1).", 
        "image": "images/projects/eco.jpg",
        "tags": ["Anglais C1", "Économie"],
        "date": "2024",
        "featured": False,
    },
    {
        "titre": "Mise en œuvre d'enquête",
        "description": "Apprentissage et application des différents types d'enquêtes statistiques.", 
        "image": "images/projects/enquete.jpg",
        "tags": ["Statistiques", "Méthodologie"],
        "date": "2025",
        "featured": False,
    },
]

# ============================================================
# FORMATION
# ============================================================

EDUCATION = [
    {
        "diplome": "BUT Science des Données",
        "etablissement": "IUT - Université de Poitiers Campus de Niort",
        "periode": "2025 - 2028",
        "mention": "En cours",
        "description": "Traiter, analyser et valoriser les données.",
    },
    {
        "diplome": "Baccalauréat (Mention Bien)",
        "etablissement": "Lycée Sainte Marthe Chavagnes",
        "periode": "2025",
        "mention": "Obtenu",
        "description": "Spécialités : NSI (Numérique), Mathématiques et Anglais AMC.",
    },
]

# --- Le reste du script (fonctions de génération) reste identique à votre structure ---
# Pensez à utiliser .splitlines() dans generate_html() pour la section 'about'.

# ============================================================
# GÉNÉRATION DES FICHIERS
# ============================================================

def generate_css():
    return """/* =====================================================
   Portfolio CSS - Thème Vert Dynamique
   =====================================================

   VARIABLES CSS GLOBALES :
   Modifiez les couleurs ici pour changer tout le site.
   --green-main   : couleur principale verte
   --green-light  : vert clair pour les survols
   --green-dark   : vert foncé pour les fonds
   --accent       : couleur d'accentuation (ici un vert néon)
   ===================================================== */

@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@400;700;800&display=swap');

:root {
  --green-main:  #22c55e;
  --green-light: #4ade80;
  --green-dark:  #14532d;
  --green-mid:   #166534;
  --green-soft:  #dcfce7;
  --accent:      #a3e635;
  --bg-dark:     #0a0f0a;
  --bg-card:     #0f1a0f;
  --bg-card2:    #111d11;
  --text-main:   #f0fdf4;
  --text-muted:  #86efac;
  --text-dim:    #4ade80;
  --border:      rgba(34,197,94,0.2);
  --glow:        rgba(34,197,94,0.15);
  --radius:      12px;
  --radius-lg:   20px;
  --transition:  0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* ---- RESET & BASE ---- */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; font-size: 16px; }

body {
  font-family: 'Space Grotesk', sans-serif;
  background-color: var(--bg-dark);
  color: var(--text-main);
  line-height: 1.6;
  overflow-x: hidden;
}

/* Grain de texture subtil en fond */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.03'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 0;
  opacity: 0.4;
}

/* ---- NAVBAR ---- */
/* La navbar devient opaque au scroll grâce au JS */
nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 1000;
  padding: 1rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  transition: var(--transition);
  background: transparent;
}

nav.scrolled {
  background: rgba(10,15,10,0.95);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
}

.nav-logo {
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: 1.4rem;
  color: var(--green-main);
  letter-spacing: -0.5px;
}

.nav-links {
  display: flex;
  gap: 2rem;
  list-style: none;
}

.nav-links a {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  letter-spacing: 0.5px;
  transition: color var(--transition);
  position: relative;
}

/* Soulignement animé au survol */
.nav-links a::after {
  content: '';
  position: absolute;
  bottom: -4px; left: 0;
  width: 0; height: 2px;
  background: var(--green-main);
  transition: width var(--transition);
}
.nav-links a:hover { color: var(--green-light); }
.nav-links a:hover::after { width: 100%; }

/* Menu hamburger mobile (affiché en <768px) */
.nav-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  flex-direction: column;
  gap: 5px;
}
.nav-toggle span {
  display: block;
  width: 24px; height: 2px;
  background: var(--green-main);
  transition: var(--transition);
}

/* ---- SECTIONS GÉNÉRALES ---- */
section {
  position: relative;
  z-index: 1;
  padding: 6rem 2rem;
  max-width: 1100px;
  margin: 0 auto;
}

.section-title {
  font-family: 'Syne', sans-serif;
  font-size: clamp(2rem, 5vw, 3rem);
  font-weight: 800;
  margin-bottom: 0.5rem;
  color: var(--text-main);
}

.section-title span {
  color: var(--green-main);
}

.section-divider {
  width: 60px; height: 4px;
  background: linear-gradient(90deg, var(--green-main), var(--accent));
  border-radius: 2px;
  margin-bottom: 3rem;
}

/* ---- HERO (SECTION D'ACCUEIL) ---- */
#hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 6rem;
  max-width: 100%;
  position: relative;
  overflow: hidden;
}

/* Cercles décoratifs en fond du hero */
#hero::before {
  content: '';
  position: absolute;
  width: 600px; height: 600px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(34,197,94,0.08) 0%, transparent 70%);
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  animation: pulse-glow 4s ease-in-out infinite;
}

@keyframes pulse-glow {
  0%, 100% { transform: translate(-50%, -50%) scale(1); opacity: 0.5; }
  50%       { transform: translate(-50%, -50%) scale(1.1); opacity: 1; }
}

.hero-inner {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 2rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}

.hero-badge {
  display: inline-block;
  background: rgba(34,197,94,0.1);
  border: 1px solid var(--border);
  color: var(--green-light);
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: 0.4rem 1rem;
  border-radius: 100px;
  margin-bottom: 1.5rem;
  /* Animation d'entrée - voir JS pour la classe 'visible' */
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.hero-title {
  font-family: 'Syne', sans-serif;
  font-size: clamp(2.5rem, 6vw, 4.5rem);
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 1rem;
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease 0.1s, transform 0.6s ease 0.1s;
}

.hero-title .name { color: var(--green-main); display: block; }

.hero-subtitle {
  font-size: 1.1rem;
  color: var(--text-muted);
  margin-bottom: 2rem;
  max-width: 480px;
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease 0.2s, transform 0.6s ease 0.2s;
}

/* La classe 'animate-in' est ajoutée par le JS au chargement */
.animate-in .hero-badge,
.animate-in .hero-title,
.animate-in .hero-subtitle,
.animate-in .hero-cta { opacity: 1; transform: translateY(0); }

.hero-cta {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease 0.3s, transform 0.6s ease 0.3s;
}

/* ---- BOUTONS ---- */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.75rem;
  border-radius: 100px;
  font-weight: 600;
  font-size: 0.95rem;
  text-decoration: none;
  transition: var(--transition);
  cursor: pointer;
  border: none;
}

.btn-primary {
  background: var(--green-main);
  color: #0a0f0a;
}
.btn-primary:hover {
  background: var(--green-light);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(34,197,94,0.3);
}

.btn-outline {
  background: transparent;
  color: var(--green-main);
  border: 1px solid var(--border);
}
.btn-outline:hover {
  background: rgba(34,197,94,0.1);
  border-color: var(--green-main);
  transform: translateY(-2px);
}

/* ---- PHOTO DE PROFIL ---- */
.hero-image-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.hero-photo-frame {
  position: relative;
  width: 320px; height: 320px;
}

/* Anneau décoratif animé autour de la photo */
.hero-photo-frame::before {
  content: '';
  position: absolute;
  inset: -8px;
  border-radius: 50%;
  background: conic-gradient(from 0deg, var(--green-main), var(--accent), var(--green-dark), var(--green-main));
  animation: spin 8s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }

.hero-photo-frame::after {
  content: '';
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  background: var(--bg-dark);
}

.hero-photo {
  position: relative;
  z-index: 1;
  width: 100%; height: 100%;
  border-radius: 50%;
  object-fit: cover;
  background: var(--bg-card);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 4rem;
  /* Fallback si pas d'image */
  color: var(--green-main);
}

.hero-photo img {
  width: 100%; height: 100%;
  border-radius: 50%;
  object-fit: cover;
}

/* Statistiques flottantes */
.hero-stats {
  position: absolute;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  right: -20px; bottom: 20px;
}

.stat-badge {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 0.5rem 1rem;
  font-size: 0.8rem;
  white-space: nowrap;
}
.stat-badge strong { color: var(--green-main); font-size: 1.1rem; display: block; }

/* ---- SECTION À PROPOS ---- */
#about {
  padding: 6rem 2rem;
  max-width: 1100px;
  margin: 0 auto;
}

.about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: start;
}

.about-text p {
  color: var(--text-muted);
  margin-bottom: 1rem;
  font-size: 1rem;
  line-height: 1.8;
}

/* Carte info avec icône */
.info-cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.info-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.25rem;
  transition: var(--transition);
}
.info-card:hover {
  border-color: var(--green-main);
  box-shadow: 0 0 20px var(--glow);
}
.info-card .icon { font-size: 1.5rem; margin-bottom: 0.5rem; }
.info-card .label { font-size: 0.75rem; color: var(--text-dim); text-transform: uppercase; letter-spacing: 1px; }
.info-card .value { font-weight: 600; font-size: 0.95rem; color: var(--text-main); }

/* ---- COMPÉTENCES ---- */
#skills { max-width: 1100px; margin: 0 auto; padding: 6rem 2rem; }

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}

.skill-item {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.25rem 1.5rem;
  transition: var(--transition);
}
.skill-item:hover { border-color: var(--green-main); transform: translateY(-3px); }

.skill-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.75rem;
}
.skill-name { font-weight: 600; }
.skill-percent { color: var(--green-main); font-weight: 700; }

/* Barre de progression CSS - animée par JS (data-level) */
.skill-bar {
  height: 6px;
  background: rgba(34,197,94,0.1);
  border-radius: 3px;
  overflow: hidden;
}
.skill-bar-fill {
  height: 100%;
  width: 0;  /* part de 0, animée par JS */
  background: linear-gradient(90deg, var(--green-main), var(--accent));
  border-radius: 3px;
  transition: width 1.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.skill-tag {
  display: inline-block;
  font-size: 0.7rem;
  color: var(--green-main);
  background: rgba(34,197,94,0.1);
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  margin-top: 0.5rem;
}

/* ---- PROJETS ---- */
#projects { max-width: 1100px; margin: 0 auto; padding: 6rem 2rem; }

/* Projet mis en avant (featured: True) */
.project-featured {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 0;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  margin-bottom: 2rem;
  transition: var(--transition);
}
.project-featured:hover { border-color: var(--green-main); box-shadow: 0 0 40px var(--glow); }

.project-featured-img {
  background: var(--bg-card2);
  min-height: 280px;
  position: relative;
  overflow: hidden;
}
.project-featured-img img {
  width: 100%; height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}
.project-featured:hover .project-featured-img img { transform: scale(1.05); }

/* Placeholder si pas d'image */
.img-placeholder {
  width: 100%; height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 4rem;
  background: linear-gradient(135deg, var(--bg-card2), var(--bg-card));
  color: var(--green-dark);
}

.project-featured-content {
  padding: 2.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.project-badge {
  display: inline-block;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--green-main);
  background: rgba(34,197,94,0.1);
  padding: 0.3rem 0.75rem;
  border-radius: 4px;
  margin-bottom: 1rem;
}

/* Grille des projets non-featured */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.project-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: var(--transition);
  display: flex;
  flex-direction: column;
}
.project-card:hover { border-color: var(--green-main); transform: translateY(-5px); box-shadow: 0 10px 40px var(--glow); }

.project-card-img {
  height: 180px;
  background: var(--bg-card2);
  position: relative;
  overflow: hidden;
}
.project-card-img img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }
.project-card:hover .project-card-img img { transform: scale(1.08); }

.project-card-body { padding: 1.5rem; flex: 1; display: flex; flex-direction: column; }
.project-card-body h3 { font-family: 'Syne', sans-serif; font-size: 1.15rem; margin-bottom: 0.5rem; }
.project-card-body p { color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; flex: 1; }

/* Tags techno */
.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 1rem 0;
}
.tag {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--green-main);
  background: rgba(34,197,94,0.08);
  border: 1px solid rgba(34,197,94,0.2);
  padding: 0.25rem 0.6rem;
  border-radius: 4px;
}

.project-links {
  display: flex;
  gap: 0.75rem;
  margin-top: 1rem;
}

.project-link {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--green-main);
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.3rem;
  transition: color var(--transition);
}
.project-link:hover { color: var(--green-light); }

/* ---- EXPÉRIENCES ---- */
#experience { max-width: 1100px; margin: 0 auto; padding: 6rem 2rem; }

/* Timeline verticale */
.timeline {
  position: relative;
  padding-left: 2rem;
}
.timeline::before {
  content: '';
  position: absolute;
  left: 0; top: 0; bottom: 0;
  width: 2px;
  background: linear-gradient(180deg, var(--green-main), transparent);
}

.timeline-item {
  position: relative;
  margin-bottom: 2.5rem;
  padding-left: 2rem;
  /* Animation au scroll - JS ajoute 'visible' */
  opacity: 0;
  transform: translateX(-20px);
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.timeline-item.visible { opacity: 1; transform: translateX(0); }

/* Point sur la timeline */
.timeline-item::before {
  content: '';
  position: absolute;
  left: -2.55rem; top: 1rem;
  width: 12px; height: 12px;
  border-radius: 50%;
  background: var(--green-main);
  box-shadow: 0 0 10px var(--green-main);
}

.timeline-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 1.75rem;
  transition: var(--transition);
}
.timeline-card:hover { border-color: var(--green-main); box-shadow: 0 0 30px var(--glow); }

.timeline-header {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 1rem;
}

.timeline-icon {
  font-size: 2rem;
  background: rgba(34,197,94,0.1);
  padding: 0.5rem;
  border-radius: var(--radius);
}

.timeline-meta h3 { font-family: 'Syne', sans-serif; font-size: 1.2rem; margin-bottom: 0.2rem; }
.timeline-company { color: var(--green-main); font-weight: 600; font-size: 0.95rem; }
.timeline-period { font-size: 0.8rem; color: var(--text-dim); margin-top: 0.2rem; }
.timeline-card p { color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; }

/* ---- FORMATION ---- */
#education { max-width: 1100px; margin: 0 auto; padding: 6rem 2rem; }

.education-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 1.5rem;
}

.edu-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 2rem;
  transition: var(--transition);
  position: relative;
  overflow: hidden;
}
.edu-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--green-main), var(--accent));
}
.edu-card:hover { border-color: var(--green-main); transform: translateY(-4px); }

.edu-period { font-size: 0.8rem; color: var(--green-main); font-weight: 600; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 0.5rem; }
.edu-card h3 { font-family: 'Syne', sans-serif; font-size: 1.2rem; margin-bottom: 0.3rem; }
.edu-school { color: var(--text-muted); font-size: 0.9rem; margin-bottom: 0.5rem; }
.edu-mention { display: inline-block; font-size: 0.75rem; color: var(--green-main); background: rgba(34,197,94,0.1); padding: 0.2rem 0.6rem; border-radius: 4px; margin-bottom: 0.75rem; }
.edu-card p { color: var(--text-dim); font-size: 0.9rem; line-height: 1.6; }

/* ---- CONTACT ---- */
#contact { max-width: 1100px; margin: 0 auto; padding: 6rem 2rem; text-align: center; }

.contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-top: 3rem;
}

.contact-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 2rem 1.5rem;
  text-decoration: none;
  color: var(--text-main);
  transition: var(--transition);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
}
.contact-card:hover { border-color: var(--green-main); transform: translateY(-5px); box-shadow: 0 10px 40px var(--glow); color: var(--green-light); }
.contact-card .icon { font-size: 2.5rem; }
.contact-card .label { font-size: 0.8rem; color: var(--text-dim); text-transform: uppercase; letter-spacing: 1px; }
.contact-card .value { font-weight: 600; font-size: 0.9rem; }

/* ---- FOOTER ---- */
footer {
  position: relative;
  z-index: 1;
  border-top: 1px solid var(--border);
  padding: 2rem;
  text-align: center;
  color: var(--text-dim);
  font-size: 0.85rem;
}

/* ---- RESPONSIVE MOBILE (< 768px) ---- */
@media (max-width: 768px) {
  .hero-inner { grid-template-columns: 1fr; text-align: center; gap: 2rem; }
  .hero-image-wrapper { order: -1; }
  .hero-photo-frame { width: 220px; height: 220px; }
  .hero-stats { display: none; }
  .hero-cta { justify-content: center; }

  .about-grid { grid-template-columns: 1fr; gap: 2rem; }
  .info-cards { grid-template-columns: 1fr 1fr; }

  .project-featured { grid-template-columns: 1fr; }
  .project-featured-img { min-height: 200px; }

  .nav-links { display: none; flex-direction: column; position: absolute; top: 100%; left: 0; right: 0; background: rgba(10,15,10,0.98); padding: 1.5rem 2rem; gap: 1rem; border-bottom: 1px solid var(--border); }
  .nav-links.open { display: flex; }
  .nav-toggle { display: flex; }
}

.exp-logo {
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #f8f9fa; /* Fond clair si le logo a du blanc */
    border-radius: 12px;
    margin-right: 20px;
    overflow: hidden;
    border: 1px solid #eee;
}

.exp-logo img {
    max-width: 100%;
    height: auto;
}
"""

def generate_js():
    return """/* =====================================================
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
"""

def render_project_image(image_path, alt="Projet"):
    """Retourne un tag <img> ou un placeholder si l'image n'existe pas encore."""
    return f"""
    <img src="{image_path}" alt="{alt}"
         onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
    <div class="img-placeholder" style="display:none;">🗂️</div>
    """

def render_featured_project(p):
    links_html = ""
    if p.get("lien_github"):
        links_html += f'<a href="{p["lien_github"]}" class="project-link" target="_blank">⬡ GitHub</a>'
    if p.get("lien_demo"):
        links_html += f'<a href="{p["lien_demo"]}" class="project-link" target="_blank">↗ Démo</a>'

    tags_html = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])

    return f"""
    <div class="project-featured">
      <div class="project-featured-img">
        {render_project_image(p['image'], p['titre'])}
      </div>
      <div class="project-featured-content">
        <span class="project-badge">⭐ Projet phare</span>
        <h3 style="font-family:'Syne',sans-serif;font-size:1.5rem;margin-bottom:0.75rem;">{p['titre']}</h3>
        <p style="color:var(--text-muted);line-height:1.7;margin-bottom:1rem;">{p['description']}</p>
        <div class="tags">{tags_html}</div>
        <div class="project-links">{links_html}</div>
        <p style="font-size:0.8rem;color:var(--text-dim);margin-top:1rem;">📅 {p['date']}</p>
      </div>
    </div>
    """

def render_project_card(p):
    links_html = ""
    if p.get("lien_github"):
        links_html += f'<a href="{p["lien_github"]}" class="project-link" target="_blank">⬡ GitHub</a>'
    if p.get("lien_demo"):
        links_html += f'<a href="{p["lien_demo"]}" class="project-link" target="_blank">↗ Démo</a>'

    tags_html = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])

    return f"""
    <div class="project-card">
      <div class="project-card-img">
        {render_project_image(p['image'], p['titre'])}
      </div>
      <div class="project-card-body">
        <h3>{p['titre']}</h3>
        <p>{p['description']}</p>
        <div class="tags">{tags_html}</div>
        <div class="project-links">
          {links_html}
          <span style="margin-left:auto;font-size:0.8rem;color:var(--text-dim);">📅 {p['date']}</span>
        </div>
      </div>
    </div>
    """

def render_skills():
    html = '<div class="skills-grid">'
    for name, level, category in SKILLS:
        html += f"""
        <div class="skill-item">
          <div class="skill-header">
            <span class="skill-name">{name}</span>
            <span class="skill-percent">{level}%</span>
          </div>
          <div class="skill-bar">
            <div class="skill-bar-fill" data-level="{level}"></div>
          </div>
          <span class="skill-tag">{category}</span>
        </div>"""
    html += '</div>'
    return html

def render_experiences():
    html = '<div class="timeline">'
    for exp in EXPERIENCES:
        html += f"""
            <div class="experience-card">
                <div class="exp-header">
                    <div class="exp-logo">
                        <img src="{exp['logo']}" alt="Logo {exp['entreprise']}" style="width:50px; height:50px; object-fit:cover; border-radius:8px;">
                    </div>
                    <div class="exp-title-container">
                        <h3>{exp['poste']}</h3>
                        <h4>{exp['entreprise']}</h4>
                    </div>
                    <span class="exp-date">{exp['periode']}</span>
                </div>
        </div>"""
    html += '</div>'
    return html

def render_education():
    html = '<div class="education-grid">'
    for edu in EDUCATION:
        html += f"""
        <div class="edu-card">
          <div class="edu-period">{edu['periode']}</div>
          <h3>{edu['diplome']}</h3>
          <div class="edu-school">🏛️ {edu['etablissement']}</div>
          <span class="edu-mention">✨ {edu['mention']}</span>
          <p>{edu['description']}</p>
        </div>"""
    html += '</div>'
    return html

def generate_html():
    # Projets
    featured_projects = [p for p in PROJECTS if p.get("featured")]
    other_projects    = [p for p in PROJECTS if not p.get("featured")]

    featured_html = "".join(render_featured_project(p) for p in featured_projects)
    grid_html     = "".join(render_project_card(p) for p in other_projects)

    # Initiales pour le placeholder de photo
    initials = "".join(w[0] for w in PERSONAL_INFO["name"].split()[:2]).upper()

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Portfolio – {PERSONAL_INFO['name']}</title>
  <meta name="description" content="Portfolio de {PERSONAL_INFO['name']} – {PERSONAL_INFO['tagline']}">
  <link rel="stylesheet" href="styles/main.css">
</head>
<body>

<!-- ======================================================
     NAVIGATION
     ====================================================== -->
<nav>
  <div class="nav-logo">{PERSONAL_INFO['name'].split()[0]}.dev</div>
  <ul class="nav-links">
    <li><a href="#about">À propos</a></li>
    <li><a href="#skills">Compétences</a></li>
    <li><a href="#projects">Projets</a></li>
    <li><a href="#experience">Expérience</a></li>
    <li><a href="#education">Formation</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
  <!-- Bouton hamburger mobile -->
  <button class="nav-toggle" aria-label="Ouvrir le menu">
    <span></span><span></span><span></span>
  </button>
</nav>

<!-- ======================================================
     HERO
     ====================================================== -->
<section id="hero">
  <div class="hero-inner">
    <div class="hero-content">
      <span class="hero-badge">🎓 {PERSONAL_INFO['tagline']}</span>
      <h1 class="hero-title">
        Bonjour, je suis
        <span class="name">{PERSONAL_INFO['name']}</span>
      </h1>
      <p class="hero-subtitle">{PERSONAL_INFO['subtitle']}</p>
      <div class="hero-cta">
        <a href="#projects" class="btn btn-primary">Voir mes projets →</a>
        <a href="#contact" class="btn btn-outline">Me contacter</a>
      </div>
    </div>

    <div class="hero-image-wrapper">
      <div class="hero-photo-frame">
        <div class="hero-photo">
          <!-- Photo : placez votre image dans images/profile.jpg -->
          <img src="{PERSONAL_INFO['photo']}" alt="Photo de profil"
               onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
          <!-- Placeholder initiales si pas de photo -->
          <div style="display:none;width:100%;height:100%;border-radius:50%;
                      background:var(--bg-card2);align-items:center;justify-content:center;
                      font-family:'Syne',sans-serif;font-size:3rem;font-weight:800;
                      color:var(--green-main);">
            {initials}
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ======================================================
     À PROPOS
     ====================================================== -->
<section id="about">
  <h2 class="section-title">À <span>propos</span></h2>
  <div class="section-divider"></div>

  <div class="about-grid">
    <div class="about-text">
      {"".join(f"<p>{para.strip()}</p>" for para in PERSONAL_INFO['about'].split('\\n') if para.strip())}
    </div>

    <div class="info-cards">
      <div class="info-card">
        <div class="icon">📍</div>
        <div class="label">Localisation</div>
        <div class="value">{PERSONAL_INFO['location']}</div>
      </div>
      <div class="info-card">
        <div class="icon">✉️</div>
        <div class="label">Email</div>
        <div class="value" style="font-size:0.82rem;">{PERSONAL_INFO['email']}</div>
      </div>
      <div class="info-card">
        <div class="icon">💼</div>
        <div class="label">Disponibilité</div>
        <div class="value">Stage / Alternance</div>
      </div>
      <div class="info-card">
        <div class="icon">🌐</div>
        <div class="label">Langues</div>
        <div class="value">FR · EN</div>
      </div>
    </div>
  </div>
</section>

<!-- ======================================================
     COMPÉTENCES
     ====================================================== -->
<section id="skills">
  <h2 class="section-title">Mes <span>compétences</span></h2>
  <div class="section-divider"></div>
  {render_skills()}
</section>

<!-- ======================================================
     PROJETS
     ====================================================== -->
<section id="projects">
  <h2 class="section-title">Mes <span>projets</span></h2>
  <div class="section-divider"></div>
  {featured_html}
  <div class="projects-grid">
    {grid_html}
  </div>
</section>

<!-- ======================================================
     EXPÉRIENCE
     ====================================================== -->
<section id="experience">
  <h2 class="section-title">Mon <span>expérience</span></h2>
  <div class="section-divider"></div>
  {render_experiences()}
</section>

<!-- ======================================================
     FORMATION
     ====================================================== -->
<section id="education">
  <h2 class="section-title">Ma <span>formation</span></h2>
  <div class="section-divider"></div>
  {render_education()}
</section>

<!-- ======================================================
     CONTACT
     ====================================================== -->
<section id="contact">
  <h2 class="section-title">Me <span>contacter</span></h2>
  <div class="section-divider" style="margin:0.5rem auto 1rem;"></div>
  <p style="color:var(--text-muted);max-width:500px;margin:0 auto;">
    Ouvert aux opportunités de stage, alternance ou collaboration. N'hésitez pas !
  </p>

  <div class="contact-grid">
    <a href="mailto:{PERSONAL_INFO['email']}" class="contact-card">
      <span class="icon">✉️</span>
      <span class="label">Email</span>
      <span class="value">{PERSONAL_INFO['email']}</span>
    </a>
    <a href="{PERSONAL_INFO['linkedin']}" class="contact-card" target="_blank">
      <span class="icon">💼</span>
      <span class="label">LinkedIn</span>
      <span class="value">Mon profil</span>
    </a>
    <a href="{PERSONAL_INFO['github']}" class="contact-card" target="_blank">
      <span class="icon">⬡</span>
      <span class="label">GitHub</span>
      <span class="value">Mon code</span>
    </a>
    <div class="contact-card">
      <span class="icon">📍</span>
      <span class="label">Localisation</span>
      <span class="value">{PERSONAL_INFO['location']}</span>
    </div>
  </div>
</section>

<!-- ======================================================
     FOOTER
     ====================================================== -->
<footer>
  <p>Fait par {PERSONAL_INFO['name']} · {PERSONAL_INFO['tagline']}</p>
  <p style="margin-top:0.5rem;font-size:0.75rem;opacity:0.5;">Fait avec Python · HTML · CSS</p>
</footer>

<script src="scripts/main.js"></script>
</body>3
</html>"""


# ============================================================
# ÉCRITURE DES FICHIERS
# ============================================================

def main():
    import os

    # Créer les dossiers si nécessaire
    os.makedirs("styles", exist_ok=True)
    os.makedirs("scripts", exist_ok=True)
    os.makedirs("images/projects", exist_ok=True)

    # Écrire les fichiers
    with open("styles/main.css", "w", encoding="utf-8") as f:
        f.write(generate_css())
    print("✅ styles/main.css généré")

    with open("scripts/main.js", "w", encoding="utf-8") as f:
        f.write(generate_js())
    print("✅ scripts/main.js généré")

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(generate_html())
    print("✅ index.html généré")

    print("""
╔══════════════════════════════════════════════╗
║         PORTFOLIO GÉNÉRÉ AVEC SUCCÈS ! 🎉   ║
╠══════════════════════════════════════════════╣
║                                              ║
║  PROCHAINES ÉTAPES :                         ║
║                                              ║
║  1. Personnalisez les données dans           ║
║     generate_portfolio.py (variables en      ║
║     haut du fichier)                         ║
║                                              ║
║  2. Ajoutez vos photos :                     ║
║     - images/profile.jpg  (votre photo)      ║
║     - images/projects/projet1.jpg ...        ║
║                                              ║
║  3. Relancez : python generate_portfolio.py  ║
║                                              ║
║  4. Ouvrez index.html dans votre navigateur  ║
║                                              ║
║  HÉBERGEMENT GRATUIT :                       ║
║  → GitHub Pages (github.com)                 ║
║  → Netlify Drop (netlify.com/drop)           ║
║                                              ║
╚══════════════════════════════════════════════╝
""")


if __name__ == "__main__":
    main()
