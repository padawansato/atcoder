str=list(input())
if str.count(str[0])==2 and str.count(str[1])==2 and str.count(str[3])==2 and str.count(str[2])==2:
    print("Yes")
elif str.count(str[0])==4 or str.count(str[2])==4 or str.count(str[1])==4 or str.count(str[3])==4:
    print("No")
else:
    print("No")
    
    
    
"""
s=input()
for i in s:
    if s.count(i)!=2:
        print('No')
        break
else:
    print('Yes')
それか
s = input()
_set = set(s)
if len(_set) == 2 and s.count(s[0]) == 2:
    print('Yes')
else:
    print('No')
# 被り文字をカウントする場合、集合を作り要素数をカウントする
# string[index]で文字を取る(インデクシング)できる。
# abc132A
""""