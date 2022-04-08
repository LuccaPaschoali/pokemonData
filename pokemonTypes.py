import pandas as pd


#getting the csv file data with pandas and adding status col
df = pd.read_csv('pokemon.csv')
df['status'] = df['attack'] + df['defense'] + df['sp_attack'] + df['sp_defense'] + df['speed'] + df['hp']

#Returns the name of the pokemons with the best status, if there is a tie code will return both names
def BestPokemon():
    dfTemp = df.sort_values(by = 'status', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')
    topStatus = dfTemp['status'].head(1)
    topStatusCount = (df.status.values == int(topStatus)).sum()
    topStatusPokemon = dfTemp[['name', 'status']].head(int(topStatusCount))
    return topStatusPokemon

#pokemons with low-tier status
#which is the fastest type?
#which is the happiest type?
#which pokemons are the hardest to catch?
#which is the weakest type?
#which is the strongest type?


