import sys
n = int(input())
N = int(input())
a = [0] * N
b = [0] * N
c = [0] * N
d = [0] * N
coin = 0
my_money = 0
for i in range(N):
    a[i], b[i], c[i], d[i] = map(int, input().split())

# 0を1にするDを最初にする


def A():
    coin += a
    return my_money * 2


def B():
    coin += b
    return my_money * 3


def C():
    coin += c
    return my_money * 5


def D():
    if n < my_money:
        coin += d
        return my_money -= 1
    elif n > my_money:
        coin += d
        return my_money += 1
    else:
        return None


D()
