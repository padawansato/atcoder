from collections import deque

nissu,yen  = map(int,input().split())
my_pic = 1
my_yen = 0
lst_pic = []
lst_yen = []
ans = 0

while nissu > 0:
    if my_yen >= yen:
        print("upgrade")
        my_yen -= yen
        lst_yen.append(my_yen)
        lst_pic.append(my_pic)
        my_pic += 1
    else:
        print("buy")
        my_yen += my_pic
        lst_yen.append(my_yen)
        lst_pic.append(my_pic)
    nissu -= 1


print(my_pic,my_yen)


print(lst_pic,lst_yen)


de_pic = deque(lst_pic)
de_yen = deque(lst_yen)
fst = 1
while de_pic:
    if fst == 1:
        p = de_pic.pop()
        ans += p-1
        fst = 0
    elif:




# 1 up-1 2 2 2 = 6