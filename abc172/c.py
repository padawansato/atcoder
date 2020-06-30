import numpy as np
N, M, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

memo = np.zeros((N, M), dtype=int)
value = int(1)  # 1冊


def rec(n, uplimit_w):
    ans = 0
    if n == N:
        return 0
    # n番目の本が読めない場合(最初から大きすぎる場合)
    elif A[n] > uplimit_w:
        # return rec(n + 1, uplimit_w)  # ここでBを試せばいいのでは？
        return rec_b(n,uplimit_w)
    # n番目の本が読める場合
    # 読んだほうがいいか読まざるほうがいいかを調べる
    else:
        ans = max(
            rec(n + 1, uplimit_w),
            rec(n + 1, uplimit_w - A[n]) + value
        )
        return ans


def rec_b(m, uplimit_w):
    ans = 0
    if m == N:
        return 0
    # n番目の本が読めない場合(最初から大きすぎる場合)
    elif B[m] > uplimit_w:
        return rec(m+ 1, uplimit_w) 
    # n番目の本が読める場合
    # 読んだほうがいいか読まざるほうがいいかを調べる
    else:
        ans = max(
            rec_b(m + 1, uplimit_w),
            rec_b(m + 1, uplimit_w - B[m]) + value
        )
        return ans


print(rec(0, K))
