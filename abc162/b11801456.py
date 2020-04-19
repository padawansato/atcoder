N=int(input())
f=N//3
b=N//5
fb=N//15
def s(x):
  return x*(x+1)//2
print(s(N) -3*s(f) -5*s(b) +15*s(fb))
print(3*s(f))