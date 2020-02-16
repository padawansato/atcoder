lst = list(map(int,input().split()))
cnt = len(set(lst))
if cnt == 2:
    print("Yes")
else:
    print("No")
