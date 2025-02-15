import requests
import pandas as pd
from urllib.parse import quote
import time
from pathlib import Path

class OpenAccessChecker:
    def __init__(self):
        self.unpaywall_email = "YOUR_EMAIL@DOMAIN.COM"  #!Remplacer par votre adresse e-mail
        self.dl_dir = Path("downloads_articles")
        self.report_dir = Path("reports")
        self.report_dir.mkdir(exist_ok=True)
        self.dl_dir.mkdir(exist_ok=True)

    def check_open_access(self, doi):
        """Vérification de l'accessibilité d'un article via son DOI"""
        encoded_doi = quote(doi)
        url = f"https://api.unpaywall.org/v2/{encoded_doi}?email={self.unpaywall_email}"

        try:
            resp = requests.get(url)
            resp.raise_for_status()
            data = resp.json()
            if data:
                best_oa_location = data.get('best_oa_location', {})
                return {
                    "is_oa": data.get("is_oa", False),
                    "pdf_url": best_oa_location.get('url') if best_oa_location else None,
                    "title": data.get('title', 'Titre inconnu'),
                }
            return None
        except requests.exceptions.RequestException as e:
            print(f"Erreur pour {doi}: {e}")
            return None

    def download_pdf(self, pdf_url, title, doi):
        """Téléchargement d'un PDF"""
        if not pdf_url:
            return False, "Pas d'URL PDF valide"

        # Nettoyage du titre pour éviter les problèmes de nom de fichier
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        pdf_path = self.dl_dir / f"{safe_title[:100]}.pdf"

        try:
            resp = requests.get(pdf_url)
            resp.raise_for_status()
            with open(pdf_path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f"Téléchargement de {doi} ({title}) effectué")
            return True, ""
        except requests.RequestException as e:
            error_message = f"Erreur pour {title}: {str(e)}"
            print(error_message)
            return False, error_message

    def get_articles(self, csv_path):
        """Récupération des articles à traiter"""
        try:
            df = pd.read_csv(csv_path)
            if "DOI" not in df.columns:
                raise ValueError("Le fichier CSV doit contenir une colonne 'DOI'")

            # Suppression des articles sans DOI
            df = df.dropna(subset=["DOI"])

            results = {
                'Nombre total d\'articles': len(df),
                'Nombre d\'articles accessibles': 0,
                'Téléchargés': 0,
                'Fail': 0
            }
            print(f"Nombre total d'articles: {len(df)}")
            report_data = []

            for _, row in df.iterrows():
                doi = row["DOI"]
                print(f"Vérification de {doi}...")

                oa_info = self.check_open_access(doi)
                if oa_info:
                    if oa_info["is_oa"]:
                        results['Nombre d\'articles accessibles'] += 1
                        print(f"Article accessible trouvé: {oa_info['title']}")

                        success, message = self.download_pdf(oa_info["pdf_url"], oa_info["title"], doi)
                        if success:
                            results['Téléchargés'] += 1
                            status = "Téléchargé avec succès"
                        else:
                            results['Fail'] += 1
                            status = f"Erreur pour {doi}: {message}"
                            print(message)
                    else:
                        status = "Payant"
                else:
                    status = "Information non disponible"

                report_data.append({
                    "DOI": doi,
                    "Titre": oa_info['title'] if oa_info else 'Titre inconnu',
                    "Statut": status,
                })
                time.sleep(1)

            report_df = pd.DataFrame(report_data)
            report_path = self.report_dir / "report.xlsx"
            report_df.to_excel(report_path, index=False)
            print(f"Rapport généré: {report_path}")

            return results
        except Exception as e:
            print(f"Erreur: {str(e)}")
            return None

def main():
    checker = OpenAccessChecker()
    # Chemin du fichier CSV
    csv_file = "references.csv"
    # Analyse des articles
    results = checker.get_articles(csv_file)

    if results:
        # Affichage d'un résumé
        print("\nRésultats:")
        print(f"Nombre total d'articles: {results['Nombre total d\'articles']}")
        print(f"Nombre d'articles accessibles: {results['Nombre d\'articles accessibles']}")
        print(f"Nombre d'articles téléchargés: {results['Téléchargés']}")
        print(f"Nombre d'articles non téléchargés: {results['Fail']}")

if __name__ == "__main__":
    main()
