a,b,c,k = map(int, input().split())
ans = 0
# a 1
# b 0
# c -1
# k 個数
cnt = k.copy()


if k == a:
    ans += k
    cnt = 0
elif k > a:
    ans += a
    cnt -= a
    if cnt < b:
        ans -= (k-a)*0
    elif k >= a+b+c :
        ans -= c
    else:
        ans -= (k-(a+b)) * c

print(ans)
