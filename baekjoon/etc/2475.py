lst = list(map(int, input().split()))
lst2 = []
for i in lst:
    lst2.append(i**2)
print(sum(lst2)%10)