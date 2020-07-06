# https://www.youtube.com/watch?v=-ZvzikEQkPY
# bit全探索
H, W, K = map(int, input().split())
c = [input() for _ in range(H)]
result = 0
"""
bit全探索
1<<HOGE=2^HOGE
根元事象が2のコインのようなものが得意
"""


for rows in range(1 << H):
    for cols in range(1 << W):
        black = 0
        # bitが1になっているか2重ループで探索
        # 赤なら黒ではないからcontinue
        # それ意外ならblackカウンタインクリメント
        for i in range(H):
            if (rows >> i) % 2 == 1:
                continue
            for j in range(W):
                if (cols >> j) % 2 == 1:
                    continue
                if c[i][j] == "#":
                    black += 1
        if black == K: # ループのなかで条件に合う場合をカウントする
            result += 1

print(result)
