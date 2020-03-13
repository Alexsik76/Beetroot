# Make a program that has some sentence (a string) on input and returns a dict
# containing all unique words as keys and the number of occurrences as values.
s = '''The house stood on a slight rise just on the edge of the village.
It stood on its own and looked over a broad spread of West Country farmland.
Not a remarkable house by any means it was about thirty years old, squattish,
squarish, made of brick, and had four windows set in the front of a size and
proportion which more or less exactly failed to please the eye.
'''
d = {}
punkt = [',', '.', '?', '\n', '!', '  ', '\t']
s = s.lower()
for i in range(len(punkt)):
    s = s.replace(punkt[i], ' ')
t = s.rsplit()
t_set = set(t)
for item in t_set:
    d[item] = s.count(item)
    print(f'{item:12}:{d[item]:3}')
