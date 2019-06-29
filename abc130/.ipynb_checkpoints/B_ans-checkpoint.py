N, X = map(int, input().split())
L = list(map(int, input().split()))
num = 1
d = 0
for i in range(N):
    d += L[i]
    if d <= X:
        num += 1
    else:
        break

print(num)
