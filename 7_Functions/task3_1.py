# A simple calculator v2.


def make_operation(op, *num):
    res = num[0]
    if op == '+':
        func = lambda a, res: res + a
    elif op == '-':
        func = lambda a, res: res - a
    elif op == '*':
        func = lambda a, res: res * a
    else:
        print('unknown operator')
        return None
    for item in num[1:]:
        res = func(item, res)
    return res


exp1 = make_operation('+', 7, 7, 2)
exp2 = make_operation('-', 5, 5, -10, -20)
exp3 = make_operation('*', 7, 6)

print(exp1, exp2, exp3, sep='\n')
