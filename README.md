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

## Fonctionnement

Le script utilise l'API [Unpaywall](https://unpaywall.org/) pour vérifier si un article est en libre accès. Si c'est le cas, il le télécharge et génère un rapport.

### Avertissement

- **Limitation des requêtes** : Unpaywall impose des limites sur le nombre de requêtes que vous pouvez effectuer. Assurez-vous de respecter ces limites pour éviter d'être bloqué.
- **Liens utiles** :
  - [Unpaywall](https://unpaywall.org/) : Pour plus d'informations sur l'API Unpaywall.
  - [Mendeley](https://www.mendeley.com/) : Pour gérer et exporter votre bibliographie.

## Dépendances

Assurez-vous d'avoir les bibliothèques suivantes installées :
- `requests`
- `pandas`

Vous pouvez les installer en utilisant pip :
```bash
pip install requests pandas
