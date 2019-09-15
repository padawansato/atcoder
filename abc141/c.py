n,k,q = map(int,input().split())
a = [] # 順番
for _ in range(q):
    a.append(int(input()))


point = [k] * n


for win in a:         # 勝った人(a[win-1])以外を下げる
    point[win-1] += 1
    for i in range(n):
        point[i] -= 1
#        print(point)

#print(point)


for i in point:
    if i <= 0:
        print("No")
    elif i >= 1:
        print("Yes")

