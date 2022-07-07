lst = [[0 for _ in range(10)] for _ in range(11)]
cnt = 0
for r in range(11):
    for c in range(10):
        lst[r][c] = cnt
        cnt += 1

print(lst)

max_val = max(map(max, lst))

print(list(map(max, lst)))
print(max_val)