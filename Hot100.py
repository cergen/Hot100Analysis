
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.min_rows', 50)
pd.set_option('display.max_rows', 100)

#dataset obtained from https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs
dfHot100 = pd.read_csv('D:\Python Coding\Hot100Analysis\hot100.csv')

#dataset for Artist Genre match obtained from
dfArtistGenre = pd.read_csv('D:\Python Coding\Hot100Analysis\MTV10000Artists\ArtistGenre_csv.csv')
dfArtistGenre

columnsToDrop = ['last-week','peak-rank','weeks-on-board']
dfHot100.drop(columnsToDrop, axis = 1, inplace = True)
dfHot100 = dfHot100[dfHot100['rank'] < 11]
dfHot100

print(list(dfArtistGenre.columns))
columnsToDrop2 = ['facebook','twitter','website','mtv']
dfArtistGenre.drop(columnsToDrop2, axis = 1, inplace = True)
dfArtistGenre

dfJoined = pd.concat([dfHot100, dfArtistGenre], axis=1, join="inner")
dfJoined