# Imports
import pandas as pd

# Create dict from CSV
conversion_data = pd.read_csv('MorseCodeConversionChart.csv')
conversion_dict = {row.Char: row.Morse for (index, row) in conversion_data.iterrows()}


# Example output for 'Hello World!': '.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--'
def convert_text(text):
    converted_text = ''
    for letter in text:
        if letter in conversion_dict:
            converted_text += f'{conversion_dict[letter]} '
        elif letter == ' ':
            converted_text += '/ '
    return converted_text


continue_conversion = True

# Program will run till user quits
while continue_conversion:
    text_input = input('Enter Text (Type exit to quit): ').upper()

    if text_input == 'EXIT':
        continue_conversion = False

    else:
        print(convert_text(text_input))

print('Goodbye!')
print(convert_text('GOODBYE!'))
