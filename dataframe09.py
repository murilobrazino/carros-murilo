import pandas as pd

# Dicionários fornecidos
german_cars = {'Company': ['Ford', 'Mercedes', 'BMW', 'Audi'], 'Price': [23845, 135925, 11995, 71400]}
japanese_cars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500, 53900]}

# 1. Criação dos DataFrames
df_german = pd.DataFrame(german_cars)
df_japanese = pd.DataFrame(japanese_cars)

#Ex . 10: Combinar dois dataframes com identificação de origem
df_combinado = pd.concat([df_german, df_japanese], keys=['german', 'japanese'])

print(df_combinado)