import pandas as pd


#getting the csv file data with pandas and adding status col
df = pd.read_csv('pokemon.csv')
df['status'] = df['attack'] + df['defense'] + df['sp_attack'] + df['sp_defense'] + df['speed'] + df['hp']

#Returns the name of the pokemons with the best status, if there is a tie code will return both names
def BestPokemon():
    topStatus = max(df['status'])
    topStatusCount = (df.status.values == int(topStatus)).sum()
    dfTemp = df.sort_values(by = 'status', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')
    topStatusPokemon = dfTemp[['name']].head(int(topStatusCount)).to_string(index=False, header=False)
    return topStatusPokemon

#pokemons with low-tier status
def WorstPokemon():
    lowStatus = min(df['status'])
    lowStatusCount = (df.status.values == int(lowStatus)).sum()
    dfTemp = df.sort_values(by = 'status', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='first')
    lowStatusPokemon = dfTemp[['name']].head(int(lowStatusCount)).to_string(index=False, header=False)
    return lowStatusPokemon

#which is the fastest type?
def FastestPokemon():
    bestSpeed = max(df['speed'])
    bestSpeedCount = (df.speed.values == int(bestSpeed)).sum()
    dfTemp = df.sort_values(by = 'speed', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')
    bestSpeedPokemon = dfTemp[['name']].head(int(bestSpeedCount)).to_string(index=False, header=False)
    return bestSpeedPokemon

#which is the happiest type?
def HappiestPokemon():
    happiestStats = max(df['base_happiness'])
    bestHappinessCount = (df.base_happiness.values == int(happiestStats)).sum()
    dfTemp = df.sort_values(by = 'base_happiness', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')
    HappiestPokemon = dfTemp[['name']].head(int(bestHappinessCount)).to_string(index=False, header=False)
    return HappiestPokemon

#which pokemons are the hardest to catch?
def HardestPokemon():
    hardestRate = min(df['capture_rate'])
    rateCount = (df.capture_rate.values == hardestRate).sum()
    dfTemp = df.sort_values(by = 'capture_rate', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='first')
    hardestPokemon = dfTemp[['name']].head(int(rateCount)).to_string(index=False, header=False)
    return hardestPokemon

#which is the weakest type?
#which is the strongest type?


print(HardestPokemon())
