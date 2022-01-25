# N = int(input())        # 맞는 것 같은데 안 됨 why?
# max_num = 0
# final_i = 0
# final_list = [N]
# for i in range(N):
#     comp = N
#     temp = 0
#     tempi = i
#     cnt = 0
#     while tempi >= 0:
#         cnt += 1
#         tempi, comp = comp - tempi, tempi
#     if max_num <= cnt:
#         max_num = cnt
#         final_i = i
#
# while final_i >= 0:
#     final_i, N = N - final_i, final_i
#     final_list.append(N)
# print(len(final_list))
# print(' '.join(map(str, final_list)))

N = int(input())
len_result = 0
result = []

for i in range(N+1):
    result_list = [N, i]
    j = 0
    while True:
        last_num = result_list[j] - result_list[j+1]
        j += 1
        if last_num < 0:
            break
        result_list.append(last_num)
        if len_result < len(result_list):
            len_result = len(result_list)
            result = result_list[:]

print(len_result)
print(' '.join(map(str, result)))