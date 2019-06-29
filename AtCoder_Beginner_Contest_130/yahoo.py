#import sys
#for line in sys.stdin:
#    print(line, end="")

from datetime import datetime
n,k = map(int, input().split())
data = [input().split() for _ in range(n)]
# 辞書に名前と個数を入れ、計算するn

dic = dict(zip(data[]))