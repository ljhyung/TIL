def solution(id_list, k):
    answer = 0
    coupon = dict()
    for day in id_list:
        user_list = list(set(day.split()))
        print(user_list)
        for user in user_list:
            if coupon.get(user)==None:
                coupon[user]=1
                answer+=1
            elif coupon.get(user)<k:
                coupon[user] += 1
                answer+=1
    return answer




print(solution(
["A B C D", "A D", "A B D", "B D"], 2))
print(solution(
["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3))

# print(solution())