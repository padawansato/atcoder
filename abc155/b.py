n = input()
lst = list(map(int,input().split()))
even = []
deny = 0

for i in lst:
    if i % 2 == 0:
        even.append(i)

for j in even:
    if j % 3 == 0 or j % 5 == 0:
        continue
    else:
        deny = 1

if deny == 0:
    print("APPROVED")
else:
    print("DENIED")


