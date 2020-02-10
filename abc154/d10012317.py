N,K = map(int,input().split())
P = list(map(int,input().split()))
Q = list()
for i in range(N-K+1):
  if i == 0:
    Q.append(sum(P[i:i+K]))
  else:
    Q.append(Q[i-1]-P[i-1]+P[i+K-1])
print((max(Q)+K)/2)
