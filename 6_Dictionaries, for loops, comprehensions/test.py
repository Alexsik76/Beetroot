arr = {"x": 2, 'y': 3,  # comment
       'z': 4}
print(arr)
print('\n', '   ', '='*14)
for key, value in arr.items():
    print('    ', '|', key, '-'*6, value, '|')
print('    ', '='*14)
print(arr.values())
print(arr.keys())
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


def func(elem):
    """ Увеличение значения каждого элемента списка """
    return elem + 10  # Возвращаем новое значение


arr = [1, 2, 3, 4, 5]
print(list(map(func, arr)))

arr1 = ['word1', 'word2', 'word3', 4]
print('-'.join(map(str, arr1)))
