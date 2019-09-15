s=list(input())
odd = ["R","U","D"]
even = ["L", "U", "D" ]

frg = 0

for i in s[0::2]:
    if i in odd:         #偶数のものが奇数番にあったらよくない
        frg += 1

for i in s[1::2]:
    if i in even:
        frg += 1

if frg == len(s):
    print("Yes")
else:
    print("No")
