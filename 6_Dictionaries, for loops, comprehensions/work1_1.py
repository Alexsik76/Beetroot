# calculator
user_input = input('Input the expression as (2+2): ')
operators = '+-*/'
for i in operators:
    if i in user_input:
        operator = user_input.find(i)
print(operator)
a = int(user_input[:operator])
b = int(user_input[operator:])
print('a, b , operator', a, b, operator)
op = user_input[operator]
dict_operators = {'+': (a + b), '-': (a - b), '*': (a * b), '/': (a / b)}
print(dict_operators[op])
# print(eval(user_input))
