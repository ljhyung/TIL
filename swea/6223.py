# _*_ coding: utf-8 _*_
#6223.py

class Circle:

    def __init__(self,r):
        self.__r = r

    @property
    def r(self):
        return self.__r

    def width(self):
        return 3.14 * self.r ** 2

ex = Circle(2)

print("원의 면적: {0}".format(ex.width()))
