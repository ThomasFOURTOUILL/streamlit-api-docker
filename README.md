# intro-api-docker
Introduction à API et Docker

## Introduction à la Session de Formation sur les API et Docker

### 1. Plan de séance :

- **Accueil des Participants**

  - Merci pour votre présence

  - Présentation brève de soi-même et de son expertise dans le domaine des API et Docker.

- **Objectifs de la Séance**
  - Objectif principal : Comprendre les bases et les applications pratiques des API et de Docker.

  - Souligner l'importance de ces technologies dans le développement moderne.

- **Vue d'Ensemble des Technologies**
  - **APIs** :
    - Brève introduction aux API (Application Programming Interfaces).
    - Leur rôle dans l'intégration de différentes applications et systèmes.

  - **Docker** :
    - Introduction à Docker et au concept des conteneurs.
    - Comment Docker facilite le déploiement et la gestion des applications.

- **Format de la Session**
  - Le déroulement de la session : 
    * Présentation théorique
    * Démonstration pratique : 
        * Démonstration avec l'application Streamlit qui intègre une API dans un environnement Docker.
        * But de la démo : Montrer comment ces technologies fonctionnent ensemble dans un cas d'utilisation réel.
    * Session de questions-réponses.

  - Encourager la participation active et les questions à tout moment.

- **Attendus de la Session**
  - Les participants obtiendront une compréhension fondamentale des API et Docker.
  - Acquérir un début de compétences pratiques à travers une démonstration en direct.

### 2. Concepts de Base : APIs et Docker

#### APIs

- **Définition d'une API**
  - **API** : Application Programming Interface.
  - Un moyen pour deux applications de communiquer entre elles.
  - Exemple : API météo utilisée pour récupérer des données météorologiques.

- **Fonctionnement des APIs**
  - Utilisent des requêtes HTTP pour communiquer.
  - Retournent des données, souvent au format JSON ou XML.
  - Exemples de méthodes HTTP : GET, POST, PUT, DELETE.

- **Utilisation des APIs**
  - Intégration de services externes (par ex. paiements, cartes).
  - Communication entre le backend et le frontend d'une application.

- **Importance des APIs**
  - Permettent la modularité et la réutilisabilité des services.
  - Facilitent l'expansion et l'intégration des systèmes.

#### Docker

- **Introduction à Docker**
  - Docker est une plateforme de conteneurisation.
  - Permet d'emballer une application et son environnement.

- **Conteneurs Docker**
  - Conteneurs : Environnements isolés pour exécuter des applications.
  - Assurent la cohérence entre les environnements de développement, test et production.

- **Images Docker**
  - Images : Modèles pour les conteneurs.
  - Contiennent le code, les outils, les bibliothèques, les variables d'environnement, etc.

- **Avantages de Docker**
  - Simplifie la configuration et évite le problème « Ça marche sur ma machine ».
  - Facilite le déploiement et la gestion d'applications.
  - Supporte l'intégration et la livraison continues (CI/CD).

#### TODO: Illustration Visuelle





  
### 3. Démonstration Pratique

- **Préparation de l'Environnement** : 
  - Configuration initiale de Docker et explication du fichier `docker-compose.yml`.
  - Mise en place d'une API simple (peut-être une API Python/FasAPI).
  
- **Création d'une Application Streamlit** :
  - Présentation du code Streamlit.
  - Démonstration de l'intégration de l'API dans l'application Streamlit.
  - Comment les conteneurs Docker interagissent entre eux (réseau Docker).

### 4. Session de Questions-Réponses (30 minutes)

- **Q&R Ouverte** : Répondre aux questions des participants sur les API, Docker, ou la démo. voir [google sheet](https://docs.google.com/spreadsheets/d/1qnE3BUOVf9qzH0fW9PzWP3ZfMzhjk9vEGkTgG87B6JE/edit#gid=0)

- **Question d'approfondissement**



## Appel de l'API depuis le terminal :

### Lancement de l'application

```sh
# construire l'application
make build

# Aller sur les port 8000 et 8005
```

```sh
# version 1
curl -X 'GET'   'http://localhost:8000/items/1?q=test' -H 'accept: ap2lication/json'

# version 2
curl -X 'GET'   'http://api:8000/items/1?q=test' -H 'accept: ap2lication/json'
```