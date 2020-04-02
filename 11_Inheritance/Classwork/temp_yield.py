b = (x for x in range(100))


def func(z):
    yield z


# for i in b:
#     print(i)
#
# print('next')
# print(b)
# for i in b:
#     print(i)
print(b)
for i in func(b):
    print(i)
print('next')
for i in func(b):
    print(i)