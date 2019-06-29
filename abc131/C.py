import fractions
A, B, C, D = map(int, input().split())
total = B - A + 1
Cdiv = B // C - (A-1) // C
Ddiv = B // D - (A-1) // D
cddiv = (C*D)//fractions.gcd(C,D)
CDdiv = B // (cddiv) - (A-1) // (cddiv)

print(total - Cdiv - Ddiv + CDdiv)
