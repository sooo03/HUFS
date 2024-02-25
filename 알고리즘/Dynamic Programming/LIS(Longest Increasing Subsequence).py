def print_IS(seq, x):
    for i in range(len(seq)):
		if x[i]: 
			print(seq[i], end="")
		else:
			print("_", end="")
	print()

def LIS_DP(seq):
	n = len(seq)
	S = [1]*n
	for i in range (1, n):
		for j in range(0, i):
			if seq[i] > seq[j] and S[i]< S[j] + 1 :
				S[i] = S[j]+1
	return max(S)

seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
lis = LIS_DP(seq)
print(lis)

'''
dp테이블인 S를 1로 채워주고 seq 리스트에서 증가하고
S에 저장된 값이 (현재 값+1)보다 작으면 S를 업데이트 시켜준다. 
이중 for문을 사용하였으므로 시간 복잡도는 O(n^2)이 된다.
'''