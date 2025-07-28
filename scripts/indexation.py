import json
import numpy as np
import faiss

# === Charger les embeddings
with open("embeddings.json", "r", encoding="utf-8") as f:
    embeddings_dict = json.load(f)

# === Convertir en tableau numpy
ids = list(embeddings_dict.keys())
vectors = np.array([embeddings_dict[i] for i in ids]).astype("float32")

# === Créer l'index FAISS
dimension = vectors.shape[1]
index = faiss.IndexFlatL2(dimension)  # L2 = distance euclidienne
index.add(vectors)

# === Sauvegarder l'index + les ids
faiss.write_index(index, "index_faiss.index")

with open("index_ids.json", "w", encoding="utf-8") as f:
    json.dump(ids, f, ensure_ascii=False, indent=2)

print("✅ Index FAISS créé et sauvegardé :")
print(" - index_faiss.index")
print(" - index_ids.json")
