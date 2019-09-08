N = int(input())
p = list(map(int, input().split()))  # 入力のときに N を使う必要はありません

p_sort = sorted(p,reverse=True)
count = 0
for i in range(N):
    if p[i] != p_sort[i]:#比べる
        count += 1
        if count == 2 and i == N-1:
            print("YES")
            exit()
        elif count >= 3:
            print("NO")
            exit()
