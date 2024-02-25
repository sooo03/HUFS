def max_sum(A, left, right):
    	# A[left], ..., A[right] 중 최대 구간 합 리턴
	m = (left+right)//2 #배열의 중간 인덱스 계산
	left_sum = 0 #왼쪽 부분 배열에서 값을 업데이트하며 합을 저장할 변수
	right_sum = 0 #오른쪽 부분 배열에서 값을 업데이트하며 합을 저장할 변수
	a = float('-inf') #왼쪽 부분 배열의 최대 합을 저장할 변수
	b = float('-inf') #오른쪽 부분 배열의 최대 합을 저장할 변수
	
	if left == right: #배열의 길이가 1인 경우 자기자신 리턴
		return A[left]
	
	#왼쪽 부분 배열에서 최대 합 계산
	for i in range(m, left-1, -1):
		left_sum += A[i]
		a = max(a, left_sum)
  
	#오른쪽 부분 배열에서 최대 합 계산
	for i in range(m+1, right+1):
		right_sum += A[i]
		b = max(b, right_sum)
  
	#왼쪽과 오른쪽으로 나누고 재귀적으로 최대 구간 합 찾음
	s = max(max_sum(A, left, m), max_sum(A, m+1, right))
 
	#왼쪽 부분 배열의 최대합, 오른쪽 부분 배열의 최대합, 중간을 포함한 부분 배열 중 최대합 고려해서 최대 구간 합 반환
	return max(a+b, s)
		
A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)
