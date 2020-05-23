import math
a, b, h, m = map(int, input().split())
c2 = m * 360 / 60
c1 = h * 360 / 12 + (1 * c2 / 12)
clis = [c1, c2]
C = max(clis) - min(clis)
# print(clis, type(C))
# C = max(clis) - min(clis) if max(clis) - \
#     min(clis) <= 180 else 360 - (max(clis) - min(clis))
# C = 360 - abs(c1 - c2) if abs(c1 - c2) > 180 else abs(c1 - c2)
# print(C, a**2, b**2, - (2 * a * b * math.cos(C)))
c = math.sqrt(a ** 2 + b ** 2 - (2 * a * b * math.cos(math.radians(C))))
print(c)
