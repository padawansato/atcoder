n = int(input())
s = list(input())
grad = 1
kcnt = 0
rcnt = 0
for tmp in s:
    if tmp == "S":
        grad += 1
        kcnt = 0
    elif tmp == "R":
        kcnt = 0
        rcnt += 1
        if rcnt == 1:
            break
    elif tmp == "K":
        if kcnt == 1:
            break
        else:
            kcnt += 1


if grad >= 5:
    print("Yes")
else:
    print("No")
