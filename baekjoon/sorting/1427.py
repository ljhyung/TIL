num = list(map(int, input()))
result = ''.join(map(str, sorted(num, reverse=True)))
print(result)