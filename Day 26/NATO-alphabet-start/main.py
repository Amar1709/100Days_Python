# Day 26 Project - NATO Alphabet


import pandas
nato_data_frame = pandas.read_csv("Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv")

#Loop through rows of a data frame

nato_dict = {row['letter']:row['code'] for index, row in nato_data_frame.iterrows()}

word = input("Enter a word: ")
word = word.upper()

nato_list = [nato_dict[letter] for letter in word]
print(nato_list)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

