n,m = map(int,input().split())
lst = list(map(int,input().split()))
syukudai = 0
while lst:
    syukudai += lst.pop()

nokori = n - syukudai
if nokori < 0:
    print("-1")
else:
    print(nokori)
# print(n,m,lst)

