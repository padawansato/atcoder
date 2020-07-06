N = int(input())
A = [int(_) for _ in input().split()]
ans = 0
AA = A + A
AA.sort(reverse=True)

# sumする
for i in range(1, N):
    ans += AA[i]

print(ans)
