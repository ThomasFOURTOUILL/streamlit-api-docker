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

#### **Préparation de l'Environnement** : 
  - Configuration initiale de Docker et explication du fichier `docker-compose.yml`.
  - Mise en place d'une API simple (peut-être une API Python/FasAPI).
  
#### **Création d'une Application Streamlit** :
  - Présentation du code Streamlit.
  - Démonstration de l'intégration de l'API dans l'application Streamlit.
  - Comment les conteneurs Docker interagissent entre eux (réseau Docker).

#### Lancement de l'application :

```sh
# construire l'application
make build

# Aller sur les port 8000 et 8005
```

Pour requêtes l'API depuis le terminal :

```sh
# version 1
curl -X 'GET'   'http://localhost:8000/items/1?q=test' -H 'accept: ap2lication/json'

# version 2
curl -X 'GET'   'http://api:8000/items/1?q=test' -H 'accept: ap2lication/json'
```

### 4. Session de Questions-Réponses

#### **Q&R** : 

Réponses aux questions des participants sur les API, Docker, ou la démo. voir [google sheet](https://docs.google.com/spreadsheets/d/1qnE3BUOVf9qzH0fW9PzWP3ZfMzhjk9vEGkTgG87B6JE/edit#gid=0).

Réponse à quelques question à la volée:

<details>
  <summary>Pour mettre une image sur Docker Hub, vous devez suivre ces étapes</summary>
    

1. **Créer un Compte sur Docker Hub** :
   - Si vous n'avez pas déjà un compte, créez-en un sur [Docker Hub](https://hub.docker.com/).

2. **Se Connecter à Docker Hub depuis votre Terminal** :
   - Ouvrez votre terminal et connectez-vous à Docker Hub en utilisant la commande :

     ```sh
     docker login
     ```
   - Entrez votre nom d'utilisateur et mot de passe de Docker Hub.

3. **Construire votre Image Docker** :
   - Assurez-vous que vous avez un `Dockerfile` pour votre application.
   - Construisez l'image avec la commande :

     ```sh
     docker build -t yourusername/imagename:tag .
     ```
   - Ici, `yourusername` est votre nom d'utilisateur sur Docker Hub, `imagename` est le nom que vous souhaitez donner à votre image, et `tag` est une étiquette pour votre image, comme `latest` ou `v1.0`.

4. **Envoyer (Push) l'Image sur Docker Hub** :
   - Utilisez la commande suivante pour envoyer l'image à Docker Hub :
     ```sh
     docker push yourusername/imagename:tag
     ```

5. **Vérifier sur Docker Hub** :
   - Une fois l'envoi terminé, connectez-vous à Docker Hub et vérifiez que votre image est bien présente dans vos dépôts (repositories).

#### A noter :
- Assurez-vous que toutes les informations sensibles ou privées sont supprimées de l'image avant de l'envoyer sur Docker Hub.
- Si votre image est destinée à un usage public, pensez à ajouter une description appropriée sur Docker Hub pour expliquer aux autres utilisateurs comment l'utiliser.
</details>

<details>
  <summary>quel est l'intéret des variables d'envrionnement et quels sont les cas pratiques de ce que l'ont peut déclarer dedans</summary>


Les variables d'environnement sont un outil puissant qui peut être utilisé pour améliorer la flexibilité, la sécurité et la maintenabilité des applications.

Les variables d'environnement sont des **variables globales** qui sont définies et accessibles à tous les processus du système d'exploitation. Elles sont utilisées pour stocker des informations de configuration, telles que les chemins d'accès aux fichiers, les identifiants de connexion, les clés API, etc.

L'intérêt des variables d'environnement est multiple :

* **Elles permettent de séparer la configuration de l'application de son code.** Cela facilite le développement et le déploiement de l'application, car les informations de configuration peuvent être modifiées sans avoir à modifier le code.
* **Elles permettent de sécuriser les informations sensibles.** Les variables d'environnement peuvent être définies avec un accès restreint, ce qui permet de protéger les informations sensibles, telles que les mots de passe, les clés API, etc.

Voici quelques exemples de ce que l'on peut déclarer dans des variables d'environnement :

* **Les chemins d'accès aux fichiers** : par exemple, le chemin d'accès au fichier de configuration de l'application, ou le chemin d'accès au dossier de stockage des données.
* **Les identifiants de connexion** : par exemple, l'identifiant et le mot de passe d'un utilisateur pour accéder à une base de données, ou l'identifiant et le secret d'un compte API.
* **Les variables d'environnement spécifiques à une application** : par exemple, le nombre d'instances de l'application à lancer, ou le niveau de journalisation de l'application.
</details>

<details>
  <summary>création d'un conteneur docker sans but précis </summary>
Il est possible de faire en sorte qu'un conteneur Docker ne fasse aucune action à l'ouverture en terminant le Dockerfile sur une commande bash vide. Par exemple, le Dockerfile suivant crée un conteneur qui ne fait rien :

```Dockerfile
FROM alpine

CMD bash
```

Ce conteneur démarrera un shell bash, qui attendra des instructions de l'utilisateur. Pour envoyer une commande à ce conteneur, il suffit d'utiliser la commande `docker exec` :

```sh
docker exec -it <nom_du_conteneur> <commande>
```

Par exemple, pour exécuter la commande `ls` dans le conteneur, on utiliserait la commande suivante :

```sh
docker exec -it <nom_du_conteneur> ls
```

Il est également possible d'utiliser un script bash pour attendre une commande (uniquement utile pour les scénarios de débogage, de test ou pour interaction manuelle). Par exemple, le script bash suivant attend une commande de l'utilisateur :

```sh
#!/bin/bash

while true; do
  echo "Attente d'une commande..."
  read commande
  echo "Commande reçue : $commande"
  eval "$commande"
done
```

Ce script peut être utilisé en fin du fichier Dockerfile sur la commande suivante :

```Dockerfile
CMD bash <chemin_vers_le_script>
```

Par exemple, pour utiliser ce script, on utiliserait le Dockerfile suivant :

```Dockerfile
FROM alpine

CMD bash /app/wait-for-command.sh
```

Ce conteneur démarrera un shell bash qui exécutera le script `wait-for-command.sh`. Le script attendra une commande de l'utilisateur, puis l'exécutera.

Pour tester, lancer la commande suivante :

```sh
# lancer le conteneur
make empty
```
</details>
