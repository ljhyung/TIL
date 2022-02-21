lst = []
for _ in range(9):
    lst.append(int(input()))
a = sum(lst)-100
def check(lst):
    for i in range(9):
        for j in range(i+1,9):
            if lst[i]+lst[j] == a:
                if i>j:
                    lst.pop(i)
                    lst.pop(j)
                else:
                    lst.pop(j)
                    lst.pop(i)
                return lst
a = check(lst)
a.sort()
for i in a:
    print(i)