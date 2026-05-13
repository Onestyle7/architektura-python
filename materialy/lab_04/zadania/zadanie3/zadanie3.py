import numpy as np

# "Baza" filmow z embeddingami (w prawdziwym systemie: OpenAI API)
filmy = {
    "Incepcja":          np.array([0.8, 0.3, 0.9]),
    "Matrix":            np.array([0.75, 0.35, 0.85]),
    "Toy Story":         np.array([0.2, 0.9, 0.1]),
    "Shrek":             np.array([0.25, 0.85, 0.15]),
    "Szeregowiec Ryan":  np.array([0.6, 0.1, 0.7]),
}

def semantic_search(query_vec, database, top_k=3):
    wyniki = []
    for tytul, wektor_filmu in database.items():
        licznik = np.dot(query_vec, wektor_filmu)
        mianownik = np.linalg.norm(query_vec) * np.linalg.norm(wektor_filmu)
        podobienstwo = licznik / mianownik

        wyniki.append((tytul, podobienstwo))

    wyniki.sort(key=lambda x: x[1], reverse=True)
    return wyniki[:top_k]

query = np.array([0.7, 0.3, 0.8])  # "cos jak sci-fi"
results = semantic_search(query, filmy, top_k=3)

for title, sim in results:
    print(f"  {title}: {sim:.3f}")