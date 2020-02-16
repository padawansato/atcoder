n = int(input())
lst = []
for _ in range(n):
    a = int(input())
    lst.append([[int(i) for i in input().split()] for _ in range(a)])
print(lst)
m = 0
for i in range(2 ** n):
    a = True
    for j in range(n):
        if i >> j & 1:
            for x, y in lst[j]:
                if (i >> (x - 1) & 1) != y:
                    a = False
                    break
    if a:
        m = max(m, bin(i).count('1'))
print(m)
