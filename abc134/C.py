N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())

max_li = sorted(A, reverse=True)


for i in A:
    if A[i] ==
print(max_li)


#     for j in A:
#         if i != j:
#             B = A.pop(j)
#             result.append(sorted(B))
#
# max = sorted(A)
# print(max)

# result = [0] * N
# escape = [0] * N
# for i in A:
#     escape[i] = int(A[i])
#     A.remove(i)
#     result[i] = sorted(A)
#     print(result[i])
#     A.insert(i,escape)
