text = 'Hello world'
print('Колличество символов в строке: ' + str(len(text)))
print('Колличество букв в строке: ' + str(len(text) - text.count(' ')))
print('В верхнем регистре: ' + text.upper())
print('В нижнем регистре: ' + text.lower())
text_upper = text.upper()
print('Текст с заглавными: ' + text_upper.capitalize())
for i in text:
    print(int(i) + '\n')
