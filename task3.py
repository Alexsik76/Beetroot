class MyIterableEven:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        rez = self.data[self.index]
        self.index += 2
        return rez


my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in MyIterableEven(my_list):
    print(i)
ml = [it for it in MyIterableEven(my_list)]
print(ml)
print(''.join(MyIterableEven(my_list)))
