'''
compute_e_ver1(n) 함수는 k!를 단순한 방법으로 O(k) 시간에 계산하는 방법이다. 따라서 O(n^2) 시간 알고리즘이다.
compute_e_ver1(n) 함수는 k!를 이전에 계산한 (k-1)! 값에 k를 곱해서 O(1) 시간에 구할 수 있다. 따라서 O(n) 시간 알고리즘이다.

time.process_time() 함수는 현재 시각을 알려준다. 예를 들어, f()의 시간을 측정하고 싶으면 다음과 같이 해야한다.
import time
before = time.process_time() #현재 시간을 얻는다
f() #함수 f를 호출한다
after = time.process_time() #현재 시간을 얻는다
print(after-before) #함수 호출 전과 후의 시간 차이(=함수 수행시간)
'''
import time, random

def compute_e_ver1(n):
	compute_1=0
	for i in range(n):
		factorial_1=1
		for j in range(1,i+1):
			compute_1 += 1/factorial_1
	return compute_1

def compute_e_ver2(n):
	compute_2=0
	factorial_2=1
	for i in range(n):
		compute_2 += 1/factorial_2
		factorial_2 *= (i+1)
	return compute_2

n=int(input('값을 입력하시오: '))

before_1=time.process_time()
compute_e_ver1(n)
after_1=time.process_time()
print(f"compute_e_ver1 함수의 실행 시간: {after_1-before_1:.5f}초")

before_2=time.process_time()
compute_e_ver2(n)
after_2=time.process_time()
print(f"compute_e_ver2 함수의 실행 시간: {after_2-before_2:.5f}초")

print(f"compute_e_ver1 함수의 실행 시간 - compute_e_ver2 함수의 실행 시간: {(after_1-before_1)-(after_2-before_2):.5f}초")
