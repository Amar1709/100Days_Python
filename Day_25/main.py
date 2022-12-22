# pylint: disable=E1101
 # pylint: disable=E1136
'''Day 25 - practice'''
import pandas as pd

df = pd.read_csv("Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(df.head())

print(df.columns)

fur_colors = df['Primary Fur Color'].value_counts()

print(fur_colors)

fur_colors.to_csv("Day 25/fur_colors.csv")
