s = 'Hello world!'
print(f'\x1b[5;32;40m{s:^40}\x1b[0m')

# The general syntax of this code is:
# \x1b[A;B;C
# A: text formatting style. It can take any value from 1 to 9.
# B: text color or foreground color. It can take any value form 30-37.
# C: background color. It can take any value form 40-47.
#
# 1,   bold
# 2,   faint
# 3,   italic
# 4,   underline
# 5,   blinking
# 6,   fast blinking
# 7,   reverse
# 8,   hide
# 9,   strikethrough
#
# Black 	   30 	40
# Red 	       31 	41
# Green 	   32 	42
# Yellow 	   33 	43
# Blue 	       34 	44
# Magenta      35 	45
# Cyan 	       36 	46
# White 	   37 	47
