def two_sum(X, Y, t):
    dic = {}
	for i in range(len(X)):
		dic[-X[i]-t] = i
	for i in range(len(Y)):
		if Y[i] in dic:
			return True
	return False
	# 함수의 내용
	

A = list(map(int, input().split())) # A 입력
B = list(map(int, input().split())) # B 입력
C = list(map(int, input().split())) # C 입력


# 함수 two_sum을 적절한 형식으로 호출해 그 결과를 이용해 결과 출력
A.sort()
for i in range(len(C)):
	a = two_sum(A, B, C[i])
	if a == True:
		print(a)
		break
	elif i == (len(C)-1):
		print(a)
	

'''
우리가 구하고자 하는 값은 two_sum 함수에서 X[i] + Y[j] = -t이므로 딕셔너리 dic을 새로 정의해서 -X[i]-t값을 저장한다. 리스트 Y의 길이만큼 돌면서, 딕셔너리에 Y[i]의 값이 있는지 확인하고 있으면 True 없으면 False를 리턴한다. 이때 딕셔너리에 값을 저장하는 for문의 수행시간은 T(n) = n, 리스트 Y의 값이 딕셔너리에 있는지 확인하는 for문의 수행시간은 T(n) = n이므로 two_sum의 수행시간은 O(n)이 된다.
입력을 받은 뒤 for문을 돌면서 two_sum에 C[i]를 넣어주며 합이 0이 되는지 확인하는 for문은 two_sum의 수행시간이 O(n)이고 조건문에서 상수시간을 사용하게 되니 결국 O(n^2)의 수행 시간을 갖게 된다.
'''
