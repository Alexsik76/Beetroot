# It is a Siple Progress Bar
import time
for i in range(101):
    print(f'[{"="*i}', f'{" "*(100-i)}]', f'{i}%', end='\r')
    time.sleep(0.2)
