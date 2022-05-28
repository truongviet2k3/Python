import random
import string # xu ly chuoi ky tu
import time  
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
str = get_valid_word(words)
print(str)

def hang_man():
    print("")