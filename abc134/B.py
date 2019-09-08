n,d  = map(int,input().split())
i = 0

while i * (2*d+1) < n:
    i += 1

print(i)