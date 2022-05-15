a,b = map(list, input().split())
a = a[::-1]
b = b[::-1]
c = a if a>b else b
c = ''.join(c)
print(c)