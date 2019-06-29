n,l = map(int,input().split())
apple = []

for i in range(n):
    apple.append(l+i)

if l <= 0:
    if n >= abs(l):
        print(0)
    else:
        print(sum(apple[:-1]))
else:
    print(sum(apple[1:]))
    