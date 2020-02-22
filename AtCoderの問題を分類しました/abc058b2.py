o=list(input())
e=list(input())+[""]
for x,y in zip(o,e):print(x+y,end="")

# zipで一つずつ取り出し、合わせて、printつなげて同じ結果を得る。