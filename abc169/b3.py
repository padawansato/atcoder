n = int(input())
a = list(map(int, input().split()))

ans = 1
if 0 in a:
    print(0)
    exit()

for i in a:
    ans *= i
    if ans > 1e18:
        break

if ans > 1e18:
    print(-1)
else:
    print(ans)
