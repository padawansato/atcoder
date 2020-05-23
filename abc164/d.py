s = int(input())
lst = [2019]
i = 1
while s > lst[-1]:
    lst.append(2019 * i)
    i += 1

print(lst)