# simple exemple readline
try:
    import readline
except ImportError:
    import pyreadline as readline
s = 'abcdesf'
print('Бажаєте змінити прізвище: ')
readline.set_startup_hook(lambda: readline.insert_text(s))
s = input('')
print(s)
