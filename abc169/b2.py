N = int(input())
A = list(input().split())
ans = 1
lim = 100000000000000000000
overflag = False

if int(Leng) > lim:
    overflag = True

for i in A:
    ans *= int(i)

if overflag is True and "0" not in A:
    print('-1')
else:
    print(ans)

print(lim)
print(Leng)
