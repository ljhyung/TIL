N = int(input())
dict = {}
for i in range(N):
    K, V = map(int, input().split())
    dict[K] = V

check = 0
area_min = 0
max_min = 0
area_max = 0
max_max = 0
max_area = 0
for i in range(min(dict.keys()), max(dict.keys())+1):

    if dict.setdefault(i, 0) != max(dict.values()):
        if dict.get(i) >= check:
            area_min += dict.get(i)
            check = dict.get(i)
        else:
            area_min += check
    else:
        max_min = i
        break
check = 0
for i in range(max(dict.keys()), min(dict.keys())-1, -1):
    if dict.setdefault(i, 0) != max(dict.values()):
        if dict.get(i) >= check:
            area_max += dict.get(i)
            check = dict.get(i)
        else:
            area_max += check
    else:
        max_max = i
        break

if max_max != max_min:
    max_area = (max_max - max_min) * max(dict.values())

print(area_min + area_max + max_area + max(dict.values()))