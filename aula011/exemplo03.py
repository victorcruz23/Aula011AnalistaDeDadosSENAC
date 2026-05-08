import pandas as pd

# importando os dados .csv

df_dados = pd.read_csv("./aula011/base1.csv", sep=";")
print (df_dados.head())

print ("\nMenor Preco")
print (df_dados["preco"].min())

print ("\nMaior Preco")
print (df_dados["preco"].max())

print ("\nTotal de Precos")
print (df_dados["preco"].sum())

print ("\nMedia Precos")
print (df_dados["preco"].mean())

