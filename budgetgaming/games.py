import pandas as pd


df = pd.read_csv('gamesps4_2021-02-05T22-43-04.csv')
df['game_price'] = df['game_price'].map(lambda x: x.lstrip('<td>').rstrip('</td>'))

print(df)


df[0]