def solution(today, terms, privacies):
    answer = []
    year, month, day = map(int, today.split('.'))
    term = {}
    for i in range(len(terms)):
        a,b = terms[i].split()
        term[a] = int(b)

    for i in range(len(privacies)):
        tyear, tmonth, tday = map(int, privacies[i][:-2].split('.'))
        endTerm = privacies[i][-1:]
        end = term[endTerm]
        if(tday-1==0):
            tday=28
            if(tmonth-1==0):
                tmonth=12
                tyear-=1
            else:
                tmonth-=1
        else:
            tday-=1
        tyear += end//12
        tmonth += end%12
        if(tmonth>12):
            tmonth-=12
            tyear += 1
        print(tyear, tmonth, tday)
        if(tyear<year or (tyear==year and tmonth<month) or (tyear==year and tmonth==month and tday<day)):
            answer.append(i+1)


    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))