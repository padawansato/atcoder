n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i],b[i] = map(int, input().split())


col = [[0] * n] * n
print(col)
# for i in range(n):
#     col[i] =