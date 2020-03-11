import readline
s = 'Сікорський'
readline.set_startup_hook(lambda: readline.insert_text(s))
s = (input('Бажаєте змінити прізвище: '))
# print(i)
print(s)
