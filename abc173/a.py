N = int(input())
sen = 1000
q = N // sen
if N > q * sen:
    print(abs(N - ((q + 1) * sen)))
else:
    print(0)
