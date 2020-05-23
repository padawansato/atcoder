t = int(input())
n = [0] * t
a = [0] * t
b = [0] * t
c = [0] * t
d = [0] * t
coin = 0
my_money = 0
for i in range(t):
    n[i], a[i], b[i], c[i], d[i] = map(int, input().split())

print(t, n, a, b, c, d)

v = [2, 3, 5, -1, 1]
w = [a[0], b[0], c[0], d[0], d[0]]
print(v, w)

lim = 10 ** 18

dp = [[0] * (n[0] + 1) for _ in range(lim)]

for i in range(n - 1, -1, -1):
    for j in range(n + 1):
        if j < w[i]:
            dp[i][j] = dp[i + 1][j]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i])

print(dp[0][n])
