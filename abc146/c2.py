a,b,x = map(int,input().split())

def can_buy(arg):
    p = a * arg + b * len(str(arg))
    return p <= x # true or false

done = 0
uncheck = 10 ** 9 + 1

while uncheck - done > 1:
    p = (uncheck+done) // 2
    if can_buy(p):
        done = p
    else:
        uncheck = p
print(done)
