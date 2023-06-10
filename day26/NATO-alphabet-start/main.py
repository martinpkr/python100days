import pandas

with open('nato_phonetic_alphabet.csv') as alphabet:
    data = pandas.read_csv(alphabet)

#Looping through dictionaries:
    word = {row.letter: row.code for (index, row) in data.iterrows()}
    print(word)
#Loop through rows of a data frame
    string = input('Write a word: ').upper()
    list = [word[letter] for letter in string]
    print(list)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

