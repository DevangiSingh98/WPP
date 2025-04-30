import pandas as pd
import numpy as np


df = pd.DataFrame({
    'John': [True, False, True, True, False, False, True, False, True, False],
    'Judy': [True, True, False, True, False, True, True, False, False, False]
})


df['party'] = df['John'] & df['Judy']


days_til_party = [None] * len(df)


next_party_day = None
for i in range(len(df) - 1, -1, -1):
    if df.loc[i, 'party']:
        next_party_day = i
        days_til_party[i] = 0
    elif next_party_day is not None:
        days_til_party[i] = next_party_day - i
    else:
        days_til_party[i] = np.nan 

df['days_til_party'] = days_til_party

print(df)
