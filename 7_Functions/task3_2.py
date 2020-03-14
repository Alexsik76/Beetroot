# A simple calculator v2.


def make_operation(op, *num):
    res1 = num[0]

    def sum1(a, res=res1):
        res += a
        return res

    def subtraction(a, res=res1):
        res -= a
        return res

    def multiplication(a, res=res1):
        global res
        res *= a
        return res

    if op == '+':
        map(sum1, num[1:])
    elif op == '-':
        map(subtraction, num[1:])
    elif op == '*':
        map(multiplication, num[1:])
    else:
        print('unknown operator')
    return res


exp1 = make_operation('+', 7, 7, 2)
exp2 = make_operation('-', 5, 5, -10, -20)
exp3 = make_operation('*', 7, 6)

print(exp1, exp2, exp3, sep='\n')
