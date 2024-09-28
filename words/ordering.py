from random import randrange, shuffle
from time import time
import pickle


def get_word(letter):
    shuffle(words)
    for w in words:
        if letter in w:
            return w


words = [
    'весло', 'мойка', 'бирка', 'гнездо', 'животное', 'зебра', 'крыша', 'папа', 'улитка', 'фрикаделька', 'хрен', 'цыпа',
    'чайник', 'щи', 'съёмка', 'эскимо', 'юла', 'яйцо',
]
diffs = []

letters = list(range(ord('а'), ord('я') + 1))
shuffle(letters)
for letter_ord in letters:
    letter = chr(letter_ord)
    word = get_word(letter)

    swap_letter = letter
    while swap_letter == letter:
        swap_letter = chr(randrange(ord('а'), ord('я') + 1))

    ind = word.index(letter)
    new_word = word[:ind] + swap_letter + word[ind + 1:]

    t = time()
    input(f'Press enter when you realise what is the correct word\n{new_word}')
    hard = time() - t
    diffs.append((letter, swap_letter, min(10, hard)))

filename = input('Enter filename to save data')
with open(f'{filename}.pickle', 'wb') as file:
    pickle.dump(diffs, file)
