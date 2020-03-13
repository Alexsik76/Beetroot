# The Guessing Game
import random
secret_num = random.randint(1, 10)
while True:
    user_num = int(input('Введите целое число от 1 до 10: '))
    if user_num == secret_num:
        print('Вы угадали')
        break
    elif user_num < secret_num:
        print('Пробуйте больше!')
    else:
        print('Пробуйте меньше!')
