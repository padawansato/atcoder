a,b,x = map(int,input().split())

price = 0
seisu = 0
while x >= a * seisu + b * len(str(seisu)):
    price =a * seisu + b * len(str(seisu))
    # print("price",price)
    # print("seisu", seisu)
    seisu += 1
if seisu-1 <= 0:
    print(0)
else:
    print(seisu-1)

# print("price",price)