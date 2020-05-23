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

v = [2, 3, 5, -1, 1]
w = [a[0], b[0], c[0], d[0], d[0]]
wv = [[w[i], v[i]] for i in range(0, 5)]
W = n[0]

print(wv)


def rec(i, uplimit_w):
    ans = 0
    if wv[i][0] > uplimit_w:
        return rec(i + 1, uplimit_w)
    else:
        ans = max(
            rec(i + 1, uplimit_w),
            rec(i + 1, uplimit_w - wv[i][0]) + wv[i][1]
        )
        return ans


def solve():
    print(rec(0, W))


def main():
    solve()


if __name__ == "__main__":
    main()
