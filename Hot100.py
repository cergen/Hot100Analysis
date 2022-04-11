
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.min_rows', 50)
pd.set_option('display.max_rows', 100)

#dataset obtained from https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs
dfHot100 = pd.read_csv('D:\Python Coding\Hot100Analysis\hot100.csv')


#top 10 df
columnsToDrop = ['last-week','peak-rank','weeks-on-board']
dfHot100.drop(columnsToDrop, axis = 1, inplace = True)
dfHot100 = dfHot100[dfHot100['rank'] < 11]
dfHot100

#top 10 unique artist and songs
unqartist = dfHot100['artist'].unique()
len(unqartist)
artistCount = dfHot100['artist'].count()
artistCount

#top 1 df
top1 = dfHot100[dfHot100['rank'] < 2]
top1

# 749 unique artists
top1['artist'].unique()
len(top1['artist'].unique())

# 1104 unique songs
top1['song'].unique()
len(top1['song'].unique())

titleWordCount = []
for track in top1['song']:
    trackL = track.lower().split()
    titleWordCount.extend(trackL)
    
dfWords = pd.DataFrame(titleWordCount, columns=['Words'])
dfWords.info()
countColumn = []
for i in range(len(dfWords['Words'])):
    countColumn.append(1)
dfWords['Count'] = countColumn
dfWords['Words'] = titleWordCount
dfWords.info()
dfWords.describe()
dfWords['Words'].unique()
wordCount = dfWords.groupby('Words').sum().sort_values(by=['Count'], ascending=False)
wordCount


#Visualize Word Count
fig, ax = plt.subplots(figsize=(8, 8))

# Plot horizontal bar graph
dfWords.sort_values(by='Count').plot.barh(x='Words',
                      y='Count',
                      ax=ax,
                      color="purple")

ax.set_title("Top Words in Billboard 100 Chart Toppers")

plt.show()
