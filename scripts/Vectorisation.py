import json
import os
from sentence_transformers import SentenceTransformer
import numpy as np

# === Charger le contenu extrait
with open("documents_textuels.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

# === Étape 1 : Découper en chunks
chunks = {}
CHUNK_SIZE = 500
chunk_id = 1

for nom_fichier, contenu in documents.items():
    contenu = contenu.replace("\n", " ")
    for i in range(0, len(contenu), CHUNK_SIZE):
        morceau = contenu[i:i + CHUNK_SIZE]
        if len(morceau.strip()) > 20:
            chunks[f"chunk_{chunk_id}"] = {
                "texte": morceau.strip(),
                "metadata": {
                    "fichier": nom_fichier,
                    "debut": i,
                    "fin": i + CHUNK_SIZE
                }
            }
            chunk_id += 1

print(f"📚 {len(chunks)} chunks créés.")

# === Étape 2 : Vectorisation avec SentenceTransformer
print("🔄 Vectorisation...")
model = SentenceTransformer("all-MiniLM-L6-v2")
textes_chunks = [chunk["texte"] for chunk in chunks.values()]
embeddings_np = model.encode(textes_chunks, show_progress_bar=True)

# === Étape 3 : Sauvegarder les chunks et les embeddings dans des fichiers lisibles
print("💾 Sauvegarde JSON...")

# chunks.json
with open("chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)

# embeddings.json
embeddings_dict = {
    chunk_id: embedding.tolist()
    for chunk_id, embedding in zip(chunks.keys(), embeddings_np)
}
with open("embeddings.json", "w", encoding="utf-8") as f:
    json.dump(embeddings_dict, f, ensure_ascii=False, indent=2)

print("✅ Fichiers créés :")
print(" - chunks.json")
print(" - embeddings.json")
