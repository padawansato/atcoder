N = int(input())
li = []
A = []
for j in range(N):
    A.append(int(input()))
    x = [0] * A[j]
    y = [0] * A[j]
    for i in range(A[j]):
        x[i], y[i] = map(int, input().split())
        x[i] -= 1
    li.append([x,y])


print(li)

ans = 0
for s in range(2 ** N):
    ok = True
    for i in range(N):
        if (s >> i & 1) == 1:
            for j in range(N):
                if li[i][j] == -1: continue
                if (s >> j & 1) != li[i][j]: ok = False
    if ok:
        # print("s = ", s)
        t = 0
        x = s
        while x > 0:
            t += x % 2
            x //= 2
        ans = max(ans, t)

print(ans)