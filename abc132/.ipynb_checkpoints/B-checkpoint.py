n = int(input())
lst = list(map(int, input().split()))
# dct = {}
# for i in range(n):
#     dct[i] = lst[i]

# ans = sorted(dct.items(), key = lambda x : x[1])
# if ans[1][0]==2:
   
cnt = 0
for i in range(n-2):
    if lst[i] < lst[i+1] < lst[i+2]\
    or lst[i] > lst[i+1] > lst[i+2]:
        cnt += 1
        
print(cnt)
       