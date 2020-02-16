import collections as col


n=int(input())
s=[input() for i in range(n)]
c = col.Counter(s)
max = max(c.values())
ans = []

for key,val in c.items():
    if val == max:
       ans.append(key)


for i in ans:
    print(i)



