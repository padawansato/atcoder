# -*- Coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)
# 再帰関数を素直に
h,w = map(int,input().split())
graph = [list(input()) for _ in range(h)]
visited = [[0 for i in range(h)] for j in range(h)]
way = [(-1,0),(1,0),(0,-1),(0,1)]

#再帰で探索
#進めるかつ訪れていないならば、1にする
def dfs(x,y):
    if x<0 or h<=x or y<0 or w<=y or graph[x][y]=="#" or  visited[x][y]:
        visited[x][y] = 1
        return 0
    for k in way:
        dfs(x+k[0],y+k[1])
        
#スタートとゴールを探す
for i in range(h):
    for j in range(w):
        if graph[i][j]=="s":
            sx,sy=i,j
        elif graph[i][j]=="g":
            gx,gy=i,j
        
dfs(sx,sy)
print("Yes") if visited[gx][gy]==1 else print("No")

