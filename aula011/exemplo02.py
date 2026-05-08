import pandas as pd

filmes = {
    "Nome do filme": ["Filme do Pelé", "Tropa de Elite", "Cidade de Deus"],
    "Data de lançamento": ["20/05/2020", "21/07/2021", "01/04/2026"],
    "Genero": ["Comedia", "Aventura", "Drama"]
}

print(filmes)
print(type(filmes))

df_filmes = pd.DataFrame(filmes)
print(df_filmes)
print("\nNome do Filme")
print(df_filmes["Nome do filme"])

