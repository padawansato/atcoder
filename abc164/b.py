a,b,c,d = map(int,input().split())

while a > 0 and c > 0:
    c = c-b
    if c <= 0 :
       break
    a = a-d



# while a>0 and c>0:
#     c = c
print("Yes" if a > c else "No")

