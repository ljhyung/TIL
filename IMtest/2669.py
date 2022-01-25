final_lst = []
final_lst_real = []
for i in range(4):
    lst = list(map(int, input().split()))
    for k in range(lst[0], lst[2]):         # 넓이 1짜리 사각형의 기준점을 왼쪽 아래 꼭지점으로 두고 겹
        for j in range(lst[1], lst[3]):
            final_lst.append([k, j])
for m in final_lst:
    if m in final_lst_real:
        pass
    else:
        final_lst_real.append(m)
print(len(final_lst_real))

