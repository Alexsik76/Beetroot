# A simple calculator.


def make_operation(op, *num):
    res = num[0]
    for i in range(1, len(num)):
        if op == '+':
            res += num[i]
        elif op == '-':
            res -= num[i]
        elif op == '*':
            res *= num[i]
        else:
            print('unknown operator')
    return res


exp1 = make_operation('+', 7, 7, 2)
exp2 = make_operation('-', 5, 5, -10, -20)
exp3 = make_operation('*', 7, 6)

print(exp1, exp2, exp3, sep='\n')
