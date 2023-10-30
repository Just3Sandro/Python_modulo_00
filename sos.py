import sys
import re

def word_to_morse(word):
    morse = {
            'A' : '.-',
            'B' : '-...',
            'C' : '-.-.',
            'D' : '-..',
            'E' : '.',
            'F' : '..-.',
            'G' : '--.',
            'H' : '....',
            'I' : '..',
            'J' : '.---',
            'K' : '-.-',
            'L' : '.-..',
            'M' : '--',
            'N' : '-.',
            'O' : '---',
            'P' : '.--.',
            'Q' : '--.-',
            'R' : '.-.',
            'S' : '...',
            'T' : '-',
            'U' : '..-',
            'V' : '...-',
            'W' : '.--',
            'X' : '-...-',
            'Y' : '-.--',
            'Z' : '--..',
            }
    morse_word = []
    for char in word:
        morse_word.append(morse[char.upper()])
    return " \ ".join(morse_word)

def trad(sentence):
    str = sentence.split(" ")
    morse_str = []
    for char in str:
        morse_str.append(word_to_morse(char))
    return " ".join(morse_str)

sentence = sys.argv[1]
traduit = trad(sentence)
print(traduit)
