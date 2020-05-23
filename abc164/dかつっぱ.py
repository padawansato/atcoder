s = input()[::-1]
sum = 0
digit = 1
cnts = [0] * 2019
cnts[0] = 1


for c in s:
    sum += int(c) * digit
    print("sum={},digit={}".format(sum,digit))
    sum %= 2019
    digit *= 10
    digit %= 2019
    cnts[sum] += 1
    print(sum)

ans = 0
for cnt in cnts:
    ans += cnt * (cnt -1) // 2

# print(ans)