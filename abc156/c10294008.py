N = int(input())
X = list(map(int, input().split()))

lower = min(X)
upper = max(X)

min_shouhi = 0
asn_zahyou = 0
for zahyou in range(lower, upper):
    shouhi = 0
    for i in range(N):
        shouhi += (X[i] - zahyou) ** 2

    if zahyou == lower:
        min_shouhi = shouhi
        asn_zahyou = zahyou
    else:
        if min_shouhi > shouhi:
            min_shouhi = shouhi
            asn_zahyou = zahyou

print(min_shouhi)
