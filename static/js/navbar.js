// // Fonction pour vérifier la route active
// function updateActiveLink() {
//     const currentRoute = window.location.pathname;

//     // Retirer la classe 'active' de tous les liens
//     const links = document.querySelectorAll("nav a");
//     links.forEach(link => link.classList.remove("active"));

//     // Ajouter la classe 'active' au lien correspondant à la route actuelle
//     if (currentRoute === '/accueil') {
//         document.getElementById('accueilLink').classList.add("active");
//     } else if (currentRoute === '/demarche') {
//         document.getElementById('demarcheLink').classList.add("active");
//     } else if (currentRoute === '/statut') {
//         document.getElementById('statutLink').classList.add("active");
//     } else if (currentRoute === '/contact') {
//         document.getElementById('contactLink').classList.add("active");
//     }
// }

// // Fonction de déconnexion
// function logOut() {
//     window.location.href = '/connexion';
// }

// // Événement pour la déconnexion
// document.getElementById('logoutButton').addEventListener('click', logOut);

// // Met à jour l'état de la navbar dès que la page est chargée
// window.addEventListener('DOMContentLoaded', updateActiveLink);

// // Écouteur pour les changements d'URL (si l'utilisateur navigue sans recharger la page)
// window.addEventListener('popstate', updateActiveLink);
