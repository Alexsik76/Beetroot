try:
    import readline
except ImportError:
    import pyreadline as readline
s = 'abcdesf'
readline.set_startup_hook(lambda: readline.insert_text(s))
input('Бажаєте змінити прізвище: ')
print(s)
s = input('')
