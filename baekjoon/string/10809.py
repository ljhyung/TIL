# S = input()
# lst = []
# for i in range(97,123):
#     try:
#         lst.append(S.index(chr(i)))
#     except ValueError:
#         lst.append(-1)
# print(' '.join(map(str, lst)))

S = input()
lst = []
for i in range(97,123):
        lst.append(S.find(chr(i)))

print(' '.join(map(str, lst)))
