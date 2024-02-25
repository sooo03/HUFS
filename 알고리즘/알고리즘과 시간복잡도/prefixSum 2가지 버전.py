import time, random

def prefixSum1(X, n):
	# code for prefixSum1 - O(n^2)
	e = 1
	for i in range(1, n+1):
		temp = 1
		for j in range(2, i+1):
			tmep *= j
		e += 1/temp
	return e
	
def prefixSum2(X, n):
	# code for prefixSum2 - O(n)
	e = 1
	temp = 1
	for i in range(1, n+1):
		temp *= i
		e += 1/temp
	return e
	
	
random.seed()		# random 함수 초기화
# n 입력받음
n = int(input())
# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
# prefixSum1 호출
before1 = time.process_time()
prefixSum1(n)
after1 = time.process_time()
# prefixSum2 호출
before2 = time.process_time()
prefixSum2(n)
after2 = time.process_time()
# 두 함수의 수행시간 출력
print("prefixSum1: ", after1-before1)
print("prefixSum2: ", after2-before2)
