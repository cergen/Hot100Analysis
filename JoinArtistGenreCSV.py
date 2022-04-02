import os
import glob
import pandas as pd

os.chdir('D:\Python Coding\Hot100Analysis\MTV10000Artists')

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

ArtistGenre_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
ArtistGenre_csv.to_csv('ArtistGenre_csv.csv', index = False, encoding = 'utf-8-sig')