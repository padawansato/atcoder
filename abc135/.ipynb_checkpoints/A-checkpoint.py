a,b  = map(int,input().split())

# k = (b+a)/2
# if isinstance(k, int) != True:
#     print("IMPOSSIBLE") 
# else:
#     print(k)
if (b+a)%2 != 0:
    print("IMPOSSIBLE")
else :
    print(int((b+a)/2))