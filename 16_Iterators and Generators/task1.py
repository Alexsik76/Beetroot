def with_index(iterable, start=0):
    i = start
    for n in iterable:
        yield i, n
        i += 1


my_dict = {'a': 1, 'b': 4, 'c': 5, 'd': 8}
for j in with_index(my_dict):
    print(j, type(j))
