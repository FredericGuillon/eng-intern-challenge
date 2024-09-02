# Frederic Guillon : Github on ydern@hotmail.com
# Update : Github account is locked. I had to create another account fork and push.
# I added in the files a screenshot of my locked github account 

# There is an error in the example given for input `.....OO.....O.O...OO...........O.OOOO.O...OO....OO.O..`
# The correct output is not 'Abc 123' but 'Abc 234'

# I did not know that part but i found out that this librairy was necessary to parse the parameters with the tests
import argparse

# English to Braille dictionary (letters and punctuation)
uk_to_b = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
}

# Braille to English dictionary (letters and punctuation)
b_to_uk = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' ',
}

# English to Braille dictionary (digits)
uk_to_b_digits = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

# Braille to English dictionary (digits)
b_to_uk_digits = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
}

# Check if it is braille or english
def is_braille(text):
    for char in text:
        if char == 'O' or char == '.':
            continue
        else:
            return False
    return True

# Choose witch way of translation will be used for the parsed parameter
def translate(text):
    if is_braille(text):
        return translate_b_to_uk(text)
    else:
        return translate_uk_to_b(text)

# Fucntion to translater text from braille to english
def translate_b_to_uk(b_text):
    uk_text = ''
    i = 0
    # setting capital mode and number mode on Off
    capital = False
    number = False
    
    #Checking all group of 6 characters 1 after the other to translate
    # Using a while loop because of the 6 digit iteration
    while i < len(b_text):
        # Catch the Capital mode
        if b_text[i:i+6] == '.....O': 
            capital = True
            i += 6
        # Catch the Number mode
        elif b_text[i:i+6] == '.O.OOO': 
            number = True
            i += 6
        # Catch the space to end numbers
        elif b_text[i:i+6] == '......':
            uk_text += ' '
            number = False
            i += 6
        # Regular translation
        else:
            if number:
                char = b_to_uk_digits.get(b_text[i:i+6], '')
            else:
                char = b_to_uk.get(b_text[i:i+6], '')
            
            if capital:
                uk_text += char.upper()
                capital = False
            else:
                uk_text += char
            i += 6
    
    return uk_text

# Fucntion to translater text from english to braille
# There is something wrong in that one because it does not work with translator.test.py
def translate_uk_to_b(uk_text):
    b_text = ''
    number = False
    
    for char in uk_text:
        if char.isupper():
            b_text += '.....O' + uk_to_b[char.lower()]
        elif char.isdigit():
            if not number: 
                b_text += '.O.OOO'
                number = True 
            b_text += uk_to_b_digits[char]
        else:
            b_text += uk_to_b.get(char.lower(), '')
            number = False
    
    return b_text


# I had to look for solutions and help of this one.
# I did not know how to make the parsing argument procedure.
def main():
    parser = argparse.ArgumentParser(description='Translate between English and Braille.')
    parser.add_argument('text', nargs='+', type=str, help='The text to translate')
    
    args = parser.parse_args()

    full_text = ' '.join(args.text)

    print(translate(full_text))

if __name__ == '__main__':
    main()

