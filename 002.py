import pandas as pd

file_path = "MURILO BRASIL CANDIDO - Automobile_data - MURILO BRASIL CANDIDO - Automobile_data.csv"
df = pd.read_csv(file_path)

print("Informações iniciais do dataset:")
print(df.info())
print("\nPrimeiras linhas:")
print(df.head(10))
print("\nValores nulos por coluna:")
print(df.isnull().sum())
print("\nLinhas com valores nulos:")
print(df[df.isnull().any(axis=1)])