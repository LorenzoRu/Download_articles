# Script de Téléchargement d'Articles Académiques

Ce script permet de vérifier l'accessibilité des articles académiques via leurs DOI et de les télécharger s'ils sont en libre accès. Il génère également un rapport des opérations effectuées.

## Prérequis

1. **Mendeley** : Réalisez votre bibliographie sur Mendeley et exportez-la en format BibTeX.
2. **Conversion BibTeX vers CSV** : Utilisez le convertisseur en ligne [BibTeX to CSV](https://www.bibtex.com/c/bibtex-to-csv-converter/) pour transformer votre fichier BibTeX en CSV.
3. **Adresse e-mail** : Remplacez `"YOUR_EMAIL@DOMAIN.COM"` dans le script par une adresse e-mail valide.

## Instructions

1. **Préparation du fichier CSV** :
   - Assurez-vous que le fichier CSV contient une colonne nommée `DOI` avec les identifiants des articles.

2. **Configuration du script** :
   - Ouvrez le script `main.py` et remplacez `"YOUR_EMAIL@DOMAIN.COM"` par votre adresse e-mail valide.

3. **Exécution du script** :
   - Lancez le script en exécutant la commande suivante dans votre terminal :
     ```bash
     python main.py
     ```
   - Le script va créer deux dossiers :
     - `downloads_articles` : Contiendra les articles téléchargés.
     - `reports` : Contiendra un fichier Excel avec le rapport des opérations effectuées.

## Environnement Virtuel (venv)

Pour éviter les conflits entre les dépendances de différents projets, il est recommandé d'utiliser un environnement virtuel. Voici comment configurer et activer un environnement virtuel sur Windows et macOS :

### Création et activation d'un environnement virtuel

#### Sur Windows

1. **Ouvrir l'invite de commandes (cmd)** :
   - Cliquez sur le bouton Démarrer et tapez "cmd".
   - Appuyez sur Entrée pour ouvrir l'invite de commandes.

2. **Naviguer vers le répertoire de votre projet** :
   - Utilisez la commande `cd` pour accéder au répertoire de votre projet. Par exemple :
     ```cmd
     cd chemin\vers\votre\projet
     ```

3. **Créer un environnement virtuel** :
   - Exécutez la commande suivante pour créer un environnement virtuel nommé `venv` :
     ```cmd
     python -m venv venv
     ```

4. **Activer l'environnement virtuel** :
   - Utilisez la commande suivante pour activer l'environnement virtuel :
     ```cmd
     venv\Scripts\activate
     ```

#### Sur macOS

1. **Ouvrir le terminal** :
   - Vous pouvez trouver le terminal dans Applications > Utilitaires > Terminal.

2. **Naviguer vers le répertoire de votre projet** :
   - Utilisez la commande `cd` pour accéder au répertoire de votre projet. Par exemple :
     ```bash
     cd chemin/vers/votre/projet
     ```

3. **Créer un environnement virtuel** :
   - Exécutez la commande suivante pour créer un environnement virtuel nommé `venv` :
     ```bash
     python3 -m venv venv
     ```

4. **Activer l'environnement virtuel** :
   - Utilisez la commande suivante pour activer l'environnement virtuel :
     ```bash
     source venv/bin/activate
     ```

### Installation des dépendances

Une fois l'environnement virtuel activé, installez les dépendances listées dans le fichier `requirements.txt` :

```bash
pip install -r requirements.txt
