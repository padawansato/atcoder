s=list(input())
s_b = s[::-1]

count = 0
ans = [0] * len(s)
for i in range(len(s)):
    if s[i] != s_b[i]:
        count += 1
        ans[i] = 1


for i in range(len(s)//2):
    if ans[i] == 1:
        s_b[i] = s[i]

#print(s_b)
print(ans.count(1)//2)
