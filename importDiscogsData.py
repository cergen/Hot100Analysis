import discogs_client
import pandas as pd
from config import *
from Hot100 import dfHot100

d = discogs_client.Client('my_user_agent/1.0', user_token = token)

dataFrame = {'name':[], 'genre':[]}
df = pd.DataFrame(d)

type(dfHot100['artist'])

artistNames = dfHot100['artist'].unique()
artistNames

songTitles = dfHot100['song'].unique()
songTitles

combinedDF = dfHot100[['song', 'artist']]
combinedDF.reset_index()

for index, row in combinedDF.iterrows():
        results = d.search(row['song'], artist=row['artist'])
        print(results[0])

print(combinedDF.iterrows())