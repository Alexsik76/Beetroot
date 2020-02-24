# Words combination
from itertools import permutations
word = input('Enter your word: ')
for item in permutations(word, len(word)):
    print(''.join(item))
