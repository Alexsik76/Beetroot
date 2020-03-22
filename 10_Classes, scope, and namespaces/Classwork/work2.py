<<<<<<< HEAD
class SomeClass(object):
    pass


def squareMethod(self, x):
    return x*x


SomeClass.square = squareMethod
obj = SomeClass()
print(obj.square(5))
print(dir(SomeClass))
=======
import glob

files = glob.glob('/home/alex/temp/*/*')
print(files)
>>>>>>> 6e7f3c4c897cbb6af95399ae826b4e793f5b6918
