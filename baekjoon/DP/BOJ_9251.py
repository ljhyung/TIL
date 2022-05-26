a = input()
b = input()
res = [0]*len(b)

for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            res[j] = (max(res[:j+1]) if max(res[:j+1])<i+1 else i) +1
print(res)
print(max(res))
