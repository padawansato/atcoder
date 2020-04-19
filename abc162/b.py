N = int(input())
lst = []

for n in range(N):
    if n % 3 == 0 or n % 5 == 0:
       # pass
        print(n)
    else:
        lst.append(n)
        # print(n)

print(sum(lst))
x = 3//3
print(x)