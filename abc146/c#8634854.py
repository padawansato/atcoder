a, b, x = list(map(int, input().split()))
ans = 0
for d in range(1, 18):
    if b * d > x:
        continue
    lower = 10 ** (d - 1)
    upper = 10 ** d
    n = (x - (b * d)) // a
    if n < upper:
        ans = max(ans, n)
ans = min(ans, 10 ** 9)
print(ans)
