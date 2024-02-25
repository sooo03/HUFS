def print_subset(x):
    	L = []
	for i in range(len(x)):
		if x[i]:
			L.append(A[i])
	print(L)

def Is_all_zero(x):
	for i in range(len(x)):
		if x[i]:
			return False
	return True

def subset_sum(k):
	global cnt
	v_sum = 0
	for i in range(len(A)):
		if x[i]:
			v_sum += A[i]
	
	if k == len(A):
		if v_sum == S:
			print_subset(x)
			cnt += 1
	else:
		# code for x[k] = 1 and x[k] = 0
		x[k] = 1
		if v_sum + A[k] <= S:
			subset_sum(k+1)
		x[k]=0
		subset_sum(k+1)
	
cnt = 0	
A = list(set(int(x) for x in input().split()))
A.sort()
S = int(input()) 
x = [0]*len(A)
subset_sum(0)

if cnt == 0:
	print("[]")
