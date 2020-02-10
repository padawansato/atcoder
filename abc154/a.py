s , t  = map(str,input().split()) #input()はstrで取る。よってintで方指定する。
a , b  = map(int,input().split()) #input()はstrで取る。よってintで方指定する。
u = input()

if u in s:
    a = a -1
elif u in t:
    b = b -1


print(a,b)