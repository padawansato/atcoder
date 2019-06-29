# -*- Coding: utf-8 -*-
N, X = map(int, input().split())
L = list(map(int,input().split()))

ans = 1
p = 0
p += L[ans]
while p <= X:
    p += L[ans]
    ans += 1

print(ans) 

# N,X = map(int,input().split())
# L = list(map(int,input().split()))

# ans = 1 #位置0も1にカウントするから
# p = 0 #今のポジション
# for i in range(N):
#     p += L[i]
#     if p <= X:
#          ans += 1
#     else:
#         break

# print(ans)        
