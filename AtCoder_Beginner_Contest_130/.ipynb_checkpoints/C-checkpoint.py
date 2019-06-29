# -*- Coding: utf-8 -*-
W,H,x,y = map(int,input().split())


if (W/2 == x) and (H/2 == y):# 中心の場合無限だから1
    print("{:.9f}".format(W*H/2),1)
else:
    print("{:.9f}".format(W*H/2),0)
     