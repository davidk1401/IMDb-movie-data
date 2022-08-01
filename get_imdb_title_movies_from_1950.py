import pandas as pd

## Import needed data
df = pd.read_csv('/Users/davidkatilius/Documents/Raw_Datasets/IMDB/title.basics.tsv', sep='\t')
pd.set_option('display.max_columns', None)


## Take a quick look at the first six rows 
df.head()

## See which titleType values are in the dataset. Only 11 total. Nothing too unusual.
df.titleType.unique()

## Shows all unique values for start year. Some seem to be integers, others are strings.
df.startYear.unique()

## There are over 9,000,000 rows in the full dataset
print(df.shape)


## Filter for only movies from 1950 or later. Around 500,000 rows in the dataset.
movies_from_1950 = df[(df['titleType'] == 'movie') & (df['startYear'] != '\\N')]
print(movies_from_1950.head())
print(movies_from_1950.shape)


## 465,226 rows in data. Trying to cast as int, but some start years remain from 1950 or earlier -- will need to look into that more later. 
df2 = movies_from_1950_1[(movies_from_1950_1['startYear'].astype('int') >= 1950)]
print(df2.head())
print(df2.shape)
movies_from_1950.startYear.unique()

## Only 9311 adult titles out of over 465,000, which have now been filtered out.
df2[(df2['isAdult'].astype('int') == 1)].shape
df3 = df2[(df2['isAdult'].astype('int') == 0)]
print(df3.head())
print(df3.shape)


# Unique columns in the runtimeMinutes column. Some movies are 10,000+ minutes long!
df3.runtimeMinutes.unique()


# Removing 'isAdult' and 'endYear' columns from dataset
df4 = pd.DataFrame(df3)
df4.pop('isAdult')
df4.pop('endYear')
df4.head(10)


# Exporting cleaned version to csv
block.to_csv(r'cleaned_title_data.csv', index=False)
