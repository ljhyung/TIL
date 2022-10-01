def solution(registered_list, new_id):
    global N, S
    answer = ''
    if new_id not in registered_list:
        return new_id
    S=''
    N=0
    visited = [0 for _ in range(999999)]
    flag = False
    for i in range(len(new_id)):
        if new_id[i].isdigit():
            S = new_id[:i]
            N = int(new_id[i:])
            flag = True
            break
    if not flag:
        S = new_id

    for i in range(len(registered_list)-1, -1, -1):
        if not registered_list[i].startswith(S):
            continue
        else:
            visited[int(registered_list[i][len(S):]) if registered_list[i][len(S):]!='' else 0] =1

    while True:
        N += 1
        if visited[N]==0:
            return S + str(N)

    return answer


# print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace14"))
# print(solution(
# ["bird99", "bird98", "bird101", "gotoxy"], "bird98"))
print(solution(
["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))
# print(solution(
# ["apple1", "orange", "banana3"], "apple"))