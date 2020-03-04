from random import choice
from string import ascii_uppercase

print(''.join(choice(ascii_uppercase) for i in range(12)))
