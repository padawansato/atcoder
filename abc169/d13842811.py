n = int(input())
r = 0
i = 2
while i * i <= n:
    j = k = 1
    while n % i == 0:
        n //= i
        j -= 1
        if j == 0:
            r += 1
            j = k = k + 1
    i += 1
print(r + (n > 1))
