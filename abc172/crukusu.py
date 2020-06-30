N, M, K = map(int, input().split())

A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
ans = 0

for i in range(1, N + 1):
    A[i] += A[i - 1]

for i in range(1, M + 1):
    B[i] += B[i - 1]


for a_cnt in range(N + 1):
    if A[a_cnt] > K:
        continue

    # b_cnt = 0
    # while b_cnt < M and A[a_cnt] + B[b_cnt] <= K:
    #     b_cnt += 1
    b_cnt = M
    while A[a_cnt] + B[b_cnt] > K:
        b_cnt -= 1

    ans = max(ans, a_cnt + b_cnt)

print(ans)
