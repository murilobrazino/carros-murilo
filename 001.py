import pandas as pd

file_path = "MURILO BRASIL CANDIDO - Automobile_data - MURILO BRASIL CANDIDO - Automobile_data.csv"
df = pd.read_csv(file_path)

print("--- PRIMEIRAS 5 LINHAS ---")
print(df.head(5))

print("\n--- ÚLTIMAS 5 LINHAS ---")
print(df.tail(5))