lst = list(map(int, input().split()))
# checka = 0
# checkb = 0
# for i in range(1, len(lst)+1):
#     if i != lst(i):
#         checka += 1
#     for j in range(len(lst),0,-1):
#         if j != lst[j]:
#             checkb += 1
#
# if checka = :
#     print('')

asc = [i for i in range(1,9)]
dsc = [i for i in range(8,0,-1)]
if lst == asc:
    print('ascending')
elif lst == dsc:
    print('descending')
else:
    print('mixed')