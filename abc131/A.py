s = list(input())

for i in range(3):
    if s[i] == s[i+1]:
        ans = "Bad"
        break
    else:
        ans = "Good"
        
print(ans)        