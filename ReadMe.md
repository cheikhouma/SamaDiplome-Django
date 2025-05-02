# SamaDiplome-Django

SamaDiplome-Django est une application web développée avec le framework Django. Elle permet aux utilisateurs de gérer leurs démarches administratives, de fournir des feedbacks, et de sécuriser leurs informations personnelles.

## Fonctionnalités

- **Gestion des démarches** : Suivi des démarches administratives.
- **Sécurité des comptes** : Gestion des mots de passe, suppression de compte, et acceptation des conditions d'utilisation.
- **Feedbacks** : Les utilisateurs peuvent laisser des commentaires et des retours.
- **Interface utilisateur** : Une interface intuitive avec des sections pour les informations personnelles, la sécurité, et les feedbacks.

## Structure du projet

Voici un aperçu de la structure du projet :

### Dossiers principaux

- **`demarche/`** : Gestion des démarches administratives.
- **`feedbacks/`** : Gestion des feedbacks des utilisateurs.
- **`securite/`** : Gestion des fonctionnalités liées à la sécurité des comptes.
- **`static/`** : Fichiers statiques (CSS, JavaScript, images).
- **`templates/`** : Templates HTML pour le rendu des pages.
- **`media/`** : Fichiers téléversés par les utilisateurs (attestations, lettres de demande).

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/cheikhouma/SamaDiplome-Django
   cd SamaDiplome-Django

2. Installez les dépendances :
    ```python
    pip install -r requirements.txt

3. Appliquez les migrations :
    ```python
    python -m manage migrate

4. Lancez le serveur de développement :
    ```python 
    python manage.py runserver 8000

5. Accédez à l'application dans votre navigateur à l'adresse : http://127.0.0.1:8000

## Utilisation
Inscription : Les utilisateurs peuvent s'inscrire via un formulaire sécurisé.
Connexion : Authentification des utilisateurs.
Gestion des informations personnelles : Modification des informations personnelles via l'interface utilisateur.
Feedbacks : Les utilisateurs peuvent soumettre des commentaires via un formulaire.
Contribution
Les contributions sont les bienvenues ! Veuillez suivre les étapes suivantes pour contribuer :