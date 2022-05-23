def solution(id_list, report, k):
    dic = dict()
    for i in range(len(id_list)):
        dic[id_list[i]]=i
    print(dic)
    dolst = [[] for _ in range(len(id_list))]
    donelst = [[] for _ in range(len(id_list))]
    for singo in report:
        do, done = singo.split(' ')
        if dic[done] not in dolst[dic[do]]:
            dolst[dic[do]] += [dic[done]]
            donelst[dic[done]] += [dic[do]]
        # lst[]
        # dic[do].add(done)
    print(dolst)
    print(donelst)
    killlist = []
    for i in range(len(donelst)):
        if len(donelst[i])>=k:
            killlist.append(i)
    print(killlist)
    answer = [0]*len(id_list)
    for k in killlist:
        for i in range(len(dolst)):
            if k in dolst[i]:
                answer[i] += 1

    return answer


a= solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
print(a)