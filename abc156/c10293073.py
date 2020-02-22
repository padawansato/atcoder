N = int(input())
X = list(map(int, input().split()))

Max = max(X)
p_min = 1000000000
for i in range(1, 101):
    p = 0
    for j in range(len(X)):
        p += (X[j] - i)**2
    if  p < p_min:
        p_min = p
    else:
        p_min = p_min
print(p_min)
