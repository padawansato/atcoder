"""
  File "/Users/e155755/Documents/compe競プロ/Atcoder/精選過去問10問/abc081/b.py", line 12, in check_even
    while lst[i] % 2 == 0:
TypeError: unsupported operand type(s) for %: 'map' and 'int'

このエラーは条件分岐のための評価式は、"A[i]　% リテラル"のようにかけない。といってる
よってenumerate(A)を使う。

"""


N = int(input())
A = list(map(int, input().split()))

ans = 0
while True:
    ok = True
    for i, a in enumerate(A):
        if a % 2 == 0:
            A[i] //= 2
        else:
            ok = False
            break
    if not ok:
        break
    ans += 1

print(ans)    
