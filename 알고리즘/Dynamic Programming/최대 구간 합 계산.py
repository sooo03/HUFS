n = int(input())
A = [int(x) for x in input().split()]
S = [A[0]]
for i in range(1, n):
	S.append(max(S[i-1]+A[i], A[i]))
print(max(S))