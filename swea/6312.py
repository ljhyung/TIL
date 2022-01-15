def mul(*num):
    total = 1
    for i in num:
        if type(i) != int:
            return "에러발생"
        else:
            total = total * i
    return total

print(mul(1, 2, '4', 3))


