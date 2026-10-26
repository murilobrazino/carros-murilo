import pandas as pd

# Carregar o conjunto de dados
df = pd.read_csv(' MURILO BRASIL CANDIDO - Automobile_data.csv')

# Calcular a quilometragem média de cada fabricante
quilometragem_media = df.groupby('company')['average-mileage'].mean()

# Imprimir o resultado
print(quilometragem_media)