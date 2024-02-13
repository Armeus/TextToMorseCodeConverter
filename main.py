# Imports
import pandas as pd

# Create dict from CSV
conversion_data = pd.read_csv('MorseCodeConversionChart.csv')
conversion_dict = {row.Char: row.Morse for (index, row) in conversion_data.iterrows()}

text = input('Enter Text: ').upper()
# Example output for 'Hello World!': '.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--'
converted_text = ''
for letter in text:
    if letter in conversion_dict:
        converted_text += f'{conversion_dict[letter]} '
    elif letter == ' ':
        converted_text += '/ '
print(converted_text)
