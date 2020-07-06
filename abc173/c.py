import numpy as np
import sys
read = sys.stdin.buffer.read
h, w, k = map(int, input().split())
# graph = [list(input())for i in range(h)]  # `.`:白 ,`#`:黒
ngraph = np.array(
    list(map(int, read().split()))).reshape((h, w))
ans = []
# for i in range(h):
#     for j in range(w):
#         if k == np.count_nonzero(ngraph="#"):
#             ans += [i, j, k]

print(ans)
print(ngraph)
