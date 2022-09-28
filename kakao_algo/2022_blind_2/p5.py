# def solution(commands):
#     answer = []
#     lst = [['' for _ in range(50+1)] for _ in range(50+1)]
#     group = [[[] for _ in range(50+1)] for _ in range(50+1)]
#     for command in commands:
#         temp = list(command.split(' '))
#         if temp[0]=='UPDATE':
#             if len(temp)==4:
#                 lst[int(temp[1])][int(temp[2])]=temp[3]
#                 for r, c in group[int(temp[1])][int(temp[2])]:
#                     lst[r][c] = temp[3]
#             else:
#                 for i in range(51):
#                     for j in range(51):
#                         if lst[i][j]==temp[1]:
#                             lst[i][j] = temp[2]
#         elif temp[0]=='MERGE':
#             # 그룹 돌면서 다 추가
#             # if group[int(temp[1])][int(temp[2])]==''
#             for r, c in group[int(temp[1])][int(temp[2])]:
#                 if [int(temp[3]),int(temp[4])] not in group[r][c]:group[r][c].append([int(temp[3]),int(temp[4])])
#                 if [r,c] not in group[int(temp[3])][int(temp[4])]:group[int(temp[3])][int(temp[4])].append([r,c])
#             for r, c in group[int(temp[3])][int(temp[4])]:
#                 if [int(temp[1]),int(temp[2])] not in group[r][c]:group[r][c].append([int(temp[1]),int(temp[2])])
#                 if [r,c] not in group[int(temp[1])][int(temp[2])]:group[int(temp[1])][int(temp[2])].append([r, c])
#             group[int(temp[1])][int(temp[2])].append([int(temp[3]),int(temp[4])])
#             group[int(temp[3])][int(temp[4])].append([int(temp[1]),int(temp[2])])
#
#             if lst[int(temp[1])][int(temp[2])]!='':
#                 lst[int(temp[3])][int(temp[4])] = lst[int(temp[1])][int(temp[2])]
#                 for r,c in group[int(temp[3])][int(temp[4])]:
#                     lst[r][c] = lst[int(temp[1])][int(temp[2])]
#             elif lst[int(temp[3])][int(temp[4])]!='':
#                 lst[int(temp[1])][int(temp[2])] = lst[int(temp[3])][int(temp[4])]
#                 for r, c in group[int(temp[1])][int(temp[2])]:
#                     lst[r][c] = lst[int(temp[3])][int(temp[4])]
#         elif temp[0]=='UNMERGE':
#             tempValue = lst[int(temp[1])][int(temp[2])]
#             for r,c in group[int(temp[1])][int(temp[2])]:
#                 lst[r][c] = ''
#             lst[int(temp[1])][int(temp[2])] = tempValue
#             for r, c in group[int(temp[1])][int(temp[2])]:
#                 group[r][c] = []
#             group[r][c] = []
#         elif temp[0]=='PRINT':
#             if lst[int(temp[1])][int(temp[2])]=='':
#                 answer.append('EMPTY')
#             else:
#                 answer.append(lst[int(temp[1])][int(temp[2])])
#     # print(lst)
#     return answer

# print(solution(
# ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))

def solution(commands):
    answer = []
    lst = [['' for _ in range(50+1)] for _ in range(50+1)]
    group = dict()
    cnt = 1
    for r in range(51):
        for j in range(51):
            group[f"{r},{j}"] = 0
    for command in commands:
        temp = list(command.split(' '))
        if temp[0]=='UPDATE':
            if len(temp)==4:
                lst[int(temp[1])][int(temp[2])]=temp[3]
                for k, v in group.items():
                    if v == group[f'{temp[1]},{temp[2]}']:
                        lst[int(k.split(',')[0])][int(k.split(',')[1])]=temp[3]

            else:
                for i in range(51):
                    for j in range(51):
                        if lst[i][j]==temp[1]:
                            lst[i][j] = temp[2]
        elif temp[0]=='MERGE':
            # 그룹 돌면서 다 추가
            # if group[int(temp[1])][int(temp[2])]==''
            tempa = group[f"{temp[1]},{temp[2]}"]
            tempb = group[f"{temp[3]},{temp[4]}"]
            if tempa==0 and tempb==0:
                newGV = cnt
                cnt += 1
            elif tempa!=0:
                newGV = tempa
            else:
                newGV = tempb
            for k, v in group.items():
                if v==tempa or v==tempb:
                    group[k] = newGV


            if lst[int(temp[1])][int(temp[2])]!='':
                lst[int(temp[3])][int(temp[4])] = lst[int(temp[1])][int(temp[2])]
                for k, v in group.items():
                    if v == newGV:
                        lst[int(k.split(',')[0])][int(k.split(',')[1])] = lst[int(temp[1])][int(temp[2])]
            elif lst[int(temp[3])][int(temp[4])]!='':
                lst[int(temp[1])][int(temp[2])] = lst[int(temp[3])][int(temp[4])]
                for k, v in group.items():
                    if v == newGV:
                        lst[int(k.split(',')[0])][int(k.split(',')[1])] = lst[int(temp[3])][int(temp[4])]
        elif temp[0]=='UNMERGE':
            tempValue = lst[int(temp[1])][int(temp[2])]
            for k, v in group.items():
                if v == group[f'{temp[1]},{temp[2]}']:
                    lst[int(k.split(',')[0])][int(k.split(',')[1])]=''
                    group[k]=0
            group[f'{temp[1]},{temp[2]}']=0
        elif temp[0]=='PRINT':
            if lst[int(temp[1])][int(temp[2])]=='':
                answer.append('EMPTY')
            else:
                answer.append(lst[int(temp[1])][int(temp[2])])
    print(lst)
    return answer
print(solution(
["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
