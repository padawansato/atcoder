n = int(input())
s = list(map(int,input().split()))

if len(s) == len(set(s)):
    print('YES')
else:
    print('NO')
