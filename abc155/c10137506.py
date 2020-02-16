from collections import Counter
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    Sss = [input().rstrip() for _ in range(N)]

    cnt = Counter(Sss)
    #print('cnt:', cnt)

    maxNum = max(cnt.values())
    #print('maxNum:', maxNum)

    anss = []
    for key, value in cnt.items():
        if value == maxNum:
            anss.append(key)
    #print('anss:', anss)

    anss.sort()

    print('\n'.join(anss))


solve()
