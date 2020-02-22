n = int(input())
lst = list(map(int,input().split()))
lst = sorted(lst)
ans = [0]*max(lst)

for p in range(min(lst),max(lst)-1): # 0 4-1
    for i,x in enumerate(lst):
        ans[p] = ans[p]+(i-p)**2

print(len(ans))
print(ans)
print(min(ans))

# print(p,po)