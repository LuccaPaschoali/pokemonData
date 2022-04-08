import pandas as pd


#getting the csv file data with pandas and adding status col
df = pd.read_csv('pokemon.csv')
df['status'] = df['attack'] + df['defense'] + df['sp_attack'] + df['sp_defense'] + df['speed'] + df['hp']

#Returns the name of the pokemons with the best status, if there is a tie code will return both names
def BestPokemon():
    topStatus = max(df['status'])
    topStatusCount = (df.status.values == int(topStatus)).sum()
    dfTemp = df.sort_values(by = 'status', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')
    topStatusPokemon = dfTemp[['name', 'status']].head(int(topStatusCount))
    return topStatusPokemon

#pokemons with low-tier status
def WorstPokemon():
    lowStatus = min(df['status'])
    lowStatusCount = (df.status.values == int(lowStatus)).sum()
    dfTemp = df.sort_values(by = 'status', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='first')
    lowStatusPokemon = dfTemp[['name', 'status']].head(int(lowStatusCount))
    return lowStatusPokemon

#which is the fastest type?
def FastestPokemon():
    bestSpeed = max(df['speed'])
    bestSpeedCount = (df.speed.values ==int(bestSpeed)).sum()
    dfTemp = df.sort_values(by = 'speed', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')
    bestSpeedPokemon = dfTemp[['name', 'speed']].head(int(bestSpeedCount))
    return bestSpeedPokemon

#which is the happiest type?
#which pokemons are the hardest to catch?
#which is the weakest type?
#which is the strongest type?


print(WorstPokemon())
print(BestPokemon())
print(FastestPokemon())