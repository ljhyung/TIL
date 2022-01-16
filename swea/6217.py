# _*_ coding: utf-8 _*_
#6217.py

class student:
    def __init__(self, name):
        self.__name = name  # 프라이빗 속성

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return "이름: {0}".format(self.__name)


class Graduatestudent(student):
    def __init__(self, name, major):
        student.__init__(self,name)
        self.__major = major  # 프라이빗 속성

    @property
    def major(self):
        return self.__major

    def __repr__(self):
        return student.__repr__(self) + ", 전공: {0}".format(self.__major)

stu1 = student("홍길동")
stu2 = Graduatestudent("이순신", "컴퓨터")

print(stu1)
print(stu2)