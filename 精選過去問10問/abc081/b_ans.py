"""
python3 b_ans.py
3          
8 12 40
[3, 2, 3]
全部を割って、一番割れなかった数を返せば、事足りる。面白い！
"""

N = int(input())
A = [int(i) for i in input().split()]
ans = [0]*N
for i in range(N):
    while A[i] % 2 == 0:
        A[i] //= 2
        ans[i] += 1
print(min(ans))
