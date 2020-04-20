n = int(input())
lst = list(map(int,input().split()))
ans = [0] * n

for i in lst:
    ans[i-1] += 1

print(*ans)