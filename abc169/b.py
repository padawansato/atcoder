N = int(input())
A = list(input().split())
ans = 1
lim = 10 ** 18


for i in range(len(A)):
    ans *= int(A[i])
if lim < ans and "0" not in A:
    print('-1')
else:
    print(ans)

# print(ans, lim)
