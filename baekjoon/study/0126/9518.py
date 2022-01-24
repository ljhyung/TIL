r, s = list(map(int, input().split()))
ls = []
cnt_seat = 0
cnt_o = 0
cnt_x = 0
cnt_max = 0
for i in range(r):
    seat = input()
    ls.append(seat)
    if '.' in seat:
        cnt_seat += 1

for row in range(r):
    for sea in range(s):
        if ls[row][sea] == 'o':
            if (row-1) >= 0 and (sea-1) >= 0:
                if ls[row-1][sea-1] == 'o':
                    cnt_o += 1
            if (row-1) >= 0:
                if ls[row-1][sea] == 'o':
                    cnt_o += 1
            if (row-1) >= 0 and (sea+1) < s:
                if ls[row-1][sea+1] == 'o':
                    cnt_o += 1

            if (sea-1) >= 0:
                if ls[row][sea-1] == 'o':
                    cnt_o += 1
            if (sea+1) < s:
                if ls[row][sea+1] == 'o':
                    cnt_o += 1

            if (row+1) < r and (sea-1) >= 0:
                if ls[row+1][sea-1] == 'o':
                    cnt_o += 1
            if (row+1) < r:
                if ls[row+1][sea] == 'o':
                    cnt_o += 1
            if (row+1) < r and (sea+1) < s:
                if ls[row+1][sea+1] == 'o':
                    cnt_o += 1
#####################################################
        if cnt_seat != 0:
            if ls[row][sea] == '.':
                cnt_x = 0
                if (row - 1) >= 0 and (sea - 1) >= 0:
                    if ls[row - 1][sea - 1] == 'o':
                        cnt_x += 1
                if (row - 1) >= 0:
                    if ls[row - 1][sea] == 'o':
                        cnt_x += 1
                if (row - 1) >= 0 and (sea + 1) < s:
                    if ls[row - 1][sea + 1] == 'o':
                        cnt_x += 1

                if (sea - 1) >= 0:
                    if ls[row][sea - 1] == 'o':
                        cnt_x += 1
                if (sea + 1) < s:
                    if ls[row][sea + 1] == 'o':
                        cnt_x += 1

                if (row + 1) < r and (sea - 1) >= 0:
                    if ls[row + 1][sea - 1] == 'o':
                        cnt_x += 1
                if (row + 1) < r:
                    if ls[row + 1][sea] == 'o':
                        cnt_x += 1
                if (row + 1) < r and (sea + 1) < s:
                    if ls[row + 1][sea + 1] == 'o':
                        cnt_x += 1
                if cnt_max < cnt_x:
                    cnt_max = cnt_x

print(int(cnt_o/2)+cnt_max)

# o에 있는거 다 더한후 /2
# x에 있는것도 다 구한 다음 젤 큰값 한번 더하기