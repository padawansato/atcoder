# 素因数分解する
n = int(input())


def factorization(n):
    arr = []
    if n == 1:
        return arr
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.appen([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


f_list = factorization(n)
ans = 0

for i in range(len(f_list)):
    _tmp = f_list[i][1]
    j = 1
    while _tmp >= 0:
        _tmp -= j
        j += 1
    ans += j - 2

print(ans)
