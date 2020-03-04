import msvcrt
import time
for i in range(101):
    print(f'[{"="*i}', f'{" "*(100-i)}]', f'{i}%', end='\r')
    if msvcrt.kbhit():
        break
    time.sleep(0.2)
print('\nExit')
