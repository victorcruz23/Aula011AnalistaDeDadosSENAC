import pandas as pd 

dados ={
    "cargos": ["assistente", "auxiliar", "gerente"],
    "salarios": [2500, 1500, 2000]
}


print(dados)
print(type(dados))

df_dados = pd.DataFrame(dados)
print(df_dados)
