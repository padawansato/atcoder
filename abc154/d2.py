n,k = map(int,input().split())
p = list(map(int,input().split()))
ans = [0]*n
win = []

# for j in range(len(p)):
#     for i in range(int(p[j])):
#         ans[j] += int(i+1) * 1/int(p[j])

for i in range(n-k+1):
    win.append(sum(ans[i:i+k]))

print(max(win))