# import sys
# def input():
# 	return sys.stdin.readline()[:-1]
# n = int(input())
# words = []
# for i in range(n):
# 	a = int(input())
# 	w = []
# 	for _ in range(a):
# 		x, y = map(int, input().split())
# 		w.append([x-1, y])
# 	words.append(w)
#
# print(words)
# ans = 0
# for bit in range(1<<n):
# 	ok = True
# 	is_honest = [(bit>>i) & 1 for i in range(n)]
# 	#print(is_honest)
# 	for i in range(n):
# 		if not is_honest[i]:
# 			continue
# 		for x, y in words[i]:
# 			if is_honest[x] != y:
# 				ok = False
# 	if ok:
# 		ans = max(ans, sum(is_honest))
# print(ans)
n = int(input())

g = [[-1 for j in range(n)] for i in range(n)]

for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        g[i][x - 1] = y

print(g)