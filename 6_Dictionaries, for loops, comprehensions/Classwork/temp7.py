some_list = [1, 2, 3]
some_dict = {
  "key_1": 1,
  "key_2": 2,
  "key_3": 3
}

some_list.append(4)
some_dict.update({"key_4": 4})
print(some_list)
print(some_dict)
for i in range(4):
    print(f'some_list = {some_list[i]}')
