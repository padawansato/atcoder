n = int(input())
lst = list(map(int, input().split()))
slst = sorted(lst)
print(abs(slst[n//2-1]-slst[(n//2)]))