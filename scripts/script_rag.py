import os
import json
import pickle
import pandas as pd
import nbformat
from PyPDF2 import PdfReader

# === Nouveau chemin du dossier unique contenant tous les fichiers
DOSSIER_COURS = r"C:\Examens\Supports programmation"

# === Dictionnaire pour stocker les textes extraits
documents = {}

# === Traitement PDF
def extraire_texte_pdf(fichier):
    texte = ""
    try:
        with open(fichier, "rb") as f:
            lecteur = PdfReader(f)
            for page in lecteur.pages:
                contenu = page.extract_text()
                if contenu:
                    texte += contenu + "\n"
    except Exception as e:
        texte = f"Erreur PDF : {e}"
    return texte

# === Traitement Notebook Jupyter
def extraire_texte_ipynb(fichier):
    texte = ""
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            notebook = nbformat.read(f, as_version=4)
            for cellule in notebook.cells:
                if cellule.cell_type in ("markdown", "code"):
                    texte += cellule.source + "\n"
    except Exception as e:
        texte = f"Erreur ipynb : {e}"
    return texte

# === Traitement CSV
def extraire_texte_csv(fichier):
    try:
        df = pd.read_csv(fichier, encoding="utf-8", errors="ignore")
        return df.head().to_string(index=False)
    except Exception as e:
        return f"Erreur CSV : {e}"

# === Traitement Pickle
def extraire_texte_pickle(fichier):
    try:
        with open(fichier, "rb") as f:
            data = pickle.load(f)
        return str(data)
    except Exception as e:
        return f"Erreur Pickle : {e}"

# === Fonction principale de traitement
def convertir_fichiers():
    if not os.path.exists(DOSSIER_COURS):
        print(f"❌ Dossier introuvable : {DOSSIER_COURS}")
        return
    print(f"📂 Contenu du dossier {DOSSIER_COURS} :")
    print(os.listdir(DOSSIER_COURS))

    for fichier_nom in os.listdir(DOSSIER_COURS):
        print(f"Fichier trouvé : {fichier_nom}")
        chemin_fichier = os.path.join(DOSSIER_COURS, fichier_nom)
        if not os.path.isfile(chemin_fichier):
            continue  # Ignore les sous-dossiers

        print(f"📄 Traitement : {chemin_fichier}")
        try:
            if fichier_nom.endswith(".pdf"):
                contenu = extraire_texte_pdf(chemin_fichier)
            elif fichier_nom.endswith(".ipynb"):
                contenu = extraire_texte_ipynb(chemin_fichier)
            elif fichier_nom.endswith(".csv"):
                contenu = extraire_texte_csv(chemin_fichier)
            elif fichier_nom.endswith((".pickle", ".pkl")):
                contenu = extraire_texte_pickle(chemin_fichier)
            else:
                print(f"⚠️  Fichier ignoré (extension non gérée) : {fichier_nom}")
                continue

            documents[fichier_nom] = contenu

        except Exception as e:
            print(f"❌ Erreur de traitement de {fichier_nom} : {e}")

# === Exécution principale
if __name__ == "__main__":
    convertir_fichiers()

    # Sauvegarde dans un fichier JSON
    with open("documents_textuels.json", "w", encoding="utf-8") as f:
        json.dump(documents, f, ensure_ascii=False, indent=2)

    print("\n✅ Conversion terminée. Les documents sont sauvegardés dans 'documents_textuels.json'.")
