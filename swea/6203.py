
class student:
    def __init__(self, ko, en, ma):
        self.__ko = ko  # 프라이빗 속성
        self.__en = en
        self.__ma = ma

    @property
    def ko(self):
        return self.__ko

    @property
    def en(self):
        return self.__en

    @property
    def ma(self):
        return self.__ma

    def sum(self):
        return "국어, 영어, 수학의 총점: {0}".format(self.__ko+self.__en+self.__ma)

grade = list(map(int, input().split(",")))
stu_grade = student(grade[0], grade[1], grade[2])
print(stu_grade.sum())