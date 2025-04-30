import pandas as pd
import numpy as np


data = {
    'date': pd.date_range(start='2025-01-01', periods=20, freq='15D'),
    'artist': np.random.choice(['Ankit Tiwari', 'Honey Singh', 'Shreya Goshal'], size=20),
    'venue': np.random.choice(['Stadium1', 'Stadium2', 'Stadium3'], size=20)
}


df = pd.DataFrame(data)


df['year_month'] = df['date'].dt.to_period('M')

concert_counts = df.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='count')


months = df['year_month'].unique()
artists = df['artist'].unique()
venues = df['venue'].unique()


all_combinations = pd.MultiIndex.from_product([months, artists, venues],
                                              names=['year_month', 'artist', 'venue'])

full_data=concert_counts.set_index(['year_month','artist','venue']).reindex(all_combinations,fill_value=0).reset_index()


wide_table= full_data.pivot(index='year_month',columns=['artist','venue'],values='count')


print(wide_table)
