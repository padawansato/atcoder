n,k,q = map(int,input().split()) #N人、Kpoint、Q回答
a = [] # 順番
for _ in range(q):
    a.append(int(input()))

# 最初に回数分引く
point = [k-q] * n

for win in a:
    point[win-1] += 1

#print(point)


for i in point:
    if i <= 0:
        print("No")
    elif i >= 1:
        print("Yes")

