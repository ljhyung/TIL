# _*_ coding: utf-8 _*_
#6225.py

class Rectangle:

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    def width(self):
        return self.__a*self.__b

ex = Rectangle(4,5)

print("사각형의 면적: {0}".format(ex.width()))