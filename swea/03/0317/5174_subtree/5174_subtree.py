import sys
from pprint import pprint

sys.stdin = open('input.txt', 'r')

def post_order(tree, start):
    res = 0
    #LRV
    if tree[start][0]:
        res += post_order(tree, tree[start][0])

    if tree[start][1]:
        res += post_order(tree, tree[start][0])

    res += 1

    return res
# ------------- 10개중 4개가 틀리는것 ------------------

def sol():
    edge_start = list(map(int, input().split()))
    #0 : 간선수, 1 : 시작 노드 번호
    tree = {}
    input_tree_data = list(map(int, input().split()))

    for i in range(edge_start[0]):
        key, value = input_tree_data[i*2], input_tree_data[i*2+1]

        if not(key in tree):
            tree[key] = [None, None]

        if not(value in tree):
            tree[value] = [None, None]

        # 1 6 6 어떤값? tree 6

        if not(tree[key][0]):
            tree[key][0] = value
            
        elif tree[key][0]:
            tree[key][1] = value

        # if tree[key][1]:
        #     tree[key].sort()

    res = post_order(tree, edge_start[1])
    return res



# ------------- 10개중 4개가 틀리는것 ------------------

# -------------- 10개중 7개 runtime err
def sol():
    edge_start = list(map(int, input().split()))
    #0 : 간선수, 1 : 시작 노드 번호
    tree = {}
    input_tree_data = list(map(int, input().split()))

    for i in range(1, 1001):
        tree[i] = [None, None]

    for i in range(edge_start[0]):
        key, value = input_tree_data[i*2], input_tree_data[i*2+1]
        #tree[key] += [value]
        if tree[key][0]:
            tree[key][1] = value
        else:
            tree[key][0] = value

        if tree[key][1]:
            tree[key].sort()

    # for i in range(1, 1001):
    #     if not(tree[i][0]):
    #         del tree[i]

    # pprint(tree)
    # print(tree[edge_start[1]])
    res = post_order(tree, edge_start[1])
    #print(res)
    return res
# -------------- 10개중 7개 runtime err

T = int(input())
for test_case in range(1, 1+T):
    print(f'#{test_case} {sol()}')