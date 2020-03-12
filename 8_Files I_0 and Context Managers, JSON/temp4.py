try:
    import readline
except ImportError:
    import pyreadline as readline
s = 'Sikorskiy'
readline.set_startup_hook((lambda: readline.insert_text(input(s))))
