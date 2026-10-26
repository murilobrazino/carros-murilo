import pandas as pd

# Carregar o conjunto de dados
df = pd.read_csv('MURILO BRASIL CANDIDO  - Automobile_data.csv')

# Encontrar o carro mais caro de cada empresa
carros_mais_caros = df.loc[df.groupby('company')['price'].idxmax()]

# Imprimir o resultado
print(carros_mais_caros[['company', 'body-style', 'price']])

