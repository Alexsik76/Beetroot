import readline
s = 'Сікорський'
readline.set_startup_hook(lambda: readline.insert_text(s))
s = (input('Бажаєте змінити прізвище: '))
print(s)
s = input('')
t = 'abcdefg'
readline.insert_text(t)
print(t)
t = input('')
readline.insert_text(t)
print(t)
