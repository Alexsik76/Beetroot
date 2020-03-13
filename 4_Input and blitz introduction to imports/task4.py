# The math quiz program
from random import randint
user_input = ''
task_qestion = 0
numbers = '0123456789'
math_func = r'+-*/^'
greating = '''   Это математическая викторина.
Вы будете получать вопросы и
программа будет оценивать ваши
ответы. Для выхода из программы
в качестве ответа наберите
"exit" '''
print(greating)
while user_input != 'exit':
    a = int(numbers[randint(0, 9)])
    b = int(numbers[randint(1, 9)])
    opp = math_func[randint(0, 4)]
    task = str(a) + opp + str(b)
    print('Итак, мой вопрос следующий: ' + task)
    if opp == '^':
        opp = '**'
    task = str(a) + opp + str(b)
    task_qestion = eval(task)
    user_input = input('Введите свой ответ: ')
    if user_input == 'exit':
        break
    if user_input == str(task_qestion):
        print('Поздравляю! Вы дали верный ответ :)')
    else:
        print('Ответ неверный :( \nВерный ответ: ' + str(task_qestion))
print('Всего хорошего')
