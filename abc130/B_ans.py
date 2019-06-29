N, X = map(int, input().split())
L = list(map(int, input().split()))

ans = 1
sum = 0

for i in range(N):
    sum += L[i]
    if sum <= X:
        num += 1
    else:
        break

print(ans)
