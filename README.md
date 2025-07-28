# Chatbot pédagogique pour l'apprentissage de la programmation

Projet réalisé dans le cadre du module Modélisation statistique pour les données complexes et le Big Data.  
Ce projet vise à développer un agent conversationnel local, destiné à accompagner les étudiants de BUT SD (Semestres 1 & 2) dans leur apprentissage des bases de la programmation.

---

## Objectif

L'agent conversationnel repose sur le principe du Retrieval Augmented Generation (RAG) : il recherche des passages pertinents dans les supports de cours vectorisés, puis génère une réponse à partir de ces éléments.  
Il fonctionne entièrement en local, sans appel à des API distantes.

---

## Fonctionnalités principales

- Extraction des contenus pédagogiques (PDF, notebooks)
- Découpage en chunks textuels pertinents
- Vectorisation des chunks avec `sentence-transformers`
- Indexation vectorielle via FAISS
- Réponses générées en s'appuyant sur les documents indexés

---

## Organisation du dépôt

├── README.md
├── requirements.txt
├── notebook_chatbot.ipynb # Notebook principal
├── scripts/ # Scripts Python pour (re)générer les données
│ ├── 01_pretraitement.py
│ ├── 02_vectorisation.py
│ └── 03_indexation.py
├── data/ # Données utilisées par le chatbot
│ ├── chunks.json
│ ├── index_ids.json
│ └── index_faiss.index


## Exécution du système

### Notebook principal

Ce projet s'exécuté sur **Google Colab** :

[[Ouvrir dans Colab](https://colab.research.google.com/drive/1-RvvVvnQiX54HnPPYuBTciGlTFdAREtL?usp=sharing)]


### Fichiers à téléverser pour exécuter le notebook

Avant d'exécuter le notebook, pensez à téléverser manuellement les fichiers suivants dans l'environnement Colab :

- `data/chunks.json`
- `data/index_ids.json`
- `data/index_faiss.index`

##  Scripts de traitement

Les scripts ci-dessous permettent de générer les fichiers nécessaires au fonctionnement du chatbot :

- `scripts/01_pretraitement.py` : extraction et nettoyage des supports (PDF, notebooks)
- `scripts/02_vectorisation.py` : vectorisation des textes via `sentence-transformers`
- `scripts/03_indexation.py` : création de l’index FAISS + fichiers `index_ids.json`

Ces scripts peuvent être lancés en local pour reconstruire complètement les données.


