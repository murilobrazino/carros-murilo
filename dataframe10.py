import pandas as pd

# German cars
german_cars = {
    'company': ['ford', 'mercedes', 'BMW', 'AUDI'],
    'price': [23845, 135925, 717995, 714600]
}

# Japanese cars
japanese_cars = {
    'company': ['toyota', 'HONDA', 'nissan', 'mitsubishi'],
    'price': [29995, 23600, 61500, 58900]
}

df_german = pd.DataFrame(german_cars)
df_japanese = pd.DataFrame(japanese_cars)

# Concatenar os dois DataFrames
df_final = pd.concat([df_german, df_japanese], ignore_index=True)

print(df_final)