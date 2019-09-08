n, k = map(int, input().split())

mod = 10**9 + 7

fac = [1, 1]
inv = [1, 1]
finv = [1, 1]
for i in range(2, n+5):
    fac.append(fac[i-1] * i % mod)
    inv.append(mod - inv[mod%i] * (mod//i) % mod)
    finv.append(finv[i-1] * inv[i] % mod)

def nck(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

for i in range(1, k+1):
    print(nck(k-1, i-1) * nck(n-k-(i-1)+i, i) % mod)
