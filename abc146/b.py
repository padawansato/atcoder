n=int(input())
s=list(input())
z=90
ans = []
# print(n,s)
# print([ord(i) for i in s])

for i in s:
    if ord(i)+n > z:
        ans.append(chr(ord("A") - (z-ord(i)-n)  -1))
    else:
        ans.append(chr(ord(i)+n))

# print([ord(i) for i in ans])
print("".join(ans))

