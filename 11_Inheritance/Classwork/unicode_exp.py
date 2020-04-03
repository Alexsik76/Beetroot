from time import sleep
s = str(b'\xF0\x9F\x9A\xB2', 'utf-8')
for i in range(50):
    print(' ', end='')
    print(s, end='')
    sleep(0.2)
    print('\b\b', end='')
# s = str(b'\xF0\x9F\x8E\xB2', 'utf-8')
# print(s, end='')

print('Hello')

