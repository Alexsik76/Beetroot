# create file JSON
try:
    import readline
except ImportError:
    import pyreadline as readline
import json
name_file1 = 'temp1.txt'
name_file2 = 'temp2.txt'
list1 = ['abc', 'def', '123', 'mnb', 'pok']
with open(name_file1, 'w') as f:
    json.dump(list1, f)
with open(name_file1) as f:
    list1 = json.load(f)
print(list1)
for i in range(len(list1)):
    print(f'Змініть значення "{list1[i]}, або натисніть "Enter"')
    s = list1[i]
    readline.set_startup_hook(lambda: readline.insert_text(s))
    print()
    s = (input(''))
    list1[i] = s
s = ''
with open(name_file2, 'w') as f:
    json.dump(list1, f)
with open(name_file1) as f:
    list1 = json.load(f)
print('Друк вмусту старого файла')
print(list1)
with open(name_file2) as f:
    list2 = json.load(f)
print('Друк вмісту нового файла')
print(list2)
