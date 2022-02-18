result = list()
for i in range(2,10):
    temp = list()
    for j in range(1,10):
        mul = i*j
        if not (mul%3) or not (mul%7):
            continue
        temp.append(mul)
    result.append(temp)

print(result)
