n, q  = map(int,input().split())
p = [0] * q
a = [0] * q
b = [0] * q
for i in range(q):
    p[i], a[i], b[i] = map(int, input().split())

print(p,a,b)