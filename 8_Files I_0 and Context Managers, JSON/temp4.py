import readline
s = 'Sik'
readline.set_startup_hook((lambda: readline.insert_text(input(s))))
