name_file = input('Введіть назву файлу:')
if name_file[-4:] != '.txt':
    name_file += '.txt'
with open(name_file, 'tw') as f:
    pass
