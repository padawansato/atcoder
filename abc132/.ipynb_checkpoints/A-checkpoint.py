str=list(input())
if str.count(str[0])==2 and str.count(str[1])==2:
    print("Yes")
elif str.count(str[0])==2 and str.count(str[2])==2:
    print("Yes")
else:
    print("No")
    