import time, random

def evaluate_n2(A, x):
	# code for O(n^2)-time function
	result = 0 # x^0 = 1
	n = len(A)
	for i in range(n):
		a_n = A[i]
		for j in range(i):
			a_n *= x
		result += a_n
	return result

	
def evaluate_n(A, x):
	# code for O(n)-time function
	result = 0 # x^0 = 1
	n = len(A)
	for i in range(n):
		result += result * x + A[i]
		return result

random.seed()		# random 함수 초기화
# n 입력받음
n = int(input('n을 입력하시오: '))
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A = [random.randint(-1000, 1000) for _ in range(n)] #계수
x = random.randint(-1000, 1000)

# evaluate_n2 호출
before1 = time.process_time()
eval_n2 = evaluate_n2(A, x)
after1 = time.process_time()
print(f'evaluate_n2의 수행시간 = {after1 - before1:.6f}초')	

# evaluate_n 호출
before2 = time.process_time()
eval_n1 = evaluate_n(A, x)
after2 = time.process_time()
print(f'evaluate_n의 수행시간 = {after2 - before2:.6f}초')

# 두 함수의 수행시간 출력