import pandas as pd

# 1. Carregar o arquivo CSV
df = pd.read_csv('MURILO BRASIL CANDIDO - Automobile_data.csv')

# 2. Ordenar os carros pelo preço em ordem crescente
df_ordenado = df.sort_values(by='price', ascending=True)

# 3. Exibir o resultado
print(df_ordenado)