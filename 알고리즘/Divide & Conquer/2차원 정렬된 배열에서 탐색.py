def find_K(A, u, d, l, r, K, result): # 행렬 A, 상하좌우 좌표(u,d,l,r), K, 좌표를 저장할 result를 바탕으로 함수 실행 
		x = (d - u) // 2 # 현재 탐색하고 있는 행렬의 x 좌표
		y = r - ( x + l ) # 현재 탐색하고 있는 행렬의 y 좌표
		
		if x >= y: # x가 y보다 크면 범위가 잘못된 것이므로 result 반환
			return result 
		elif A[u+x][l+x] == K: # x == K인 경우 정답이므로 return
			return (u+x,l+x) # 
		elif A[u+y][l+y] == K: # y == K인 경우 정답이므로 return
			return (u+y, l+y) # 
		elif A[u+x][l+x] > K: # x < K인 경우 4사분면에는 K가 없으므로 1,2,3사분면 탐색
			result = find_K(A, u, u + x, l + y, r, K, result) # 1사분면
			result = find_K(A, u, u + x, l, l + x, K, result) # 2사분면
			result = find_K(A, u + y, d, l, l + x, K, result) # 3사분면
		elif A[u + y][l + y] < K: # y < K인 경우 2사분면에는 K가 없으므로 1,3,4사분면 탐색
			result = find_K(A, u, u + x, l + y, r, K, result) # 1사분면
			result = find_K(A, u + y, d, l, l + x, K, result) # 3사분면
			result = find_K(A, u + y, d, l + y, r, K, result) # 4사분면
		elif A[u + x][l + x] < K < A[u + y][l + y]: # x < K < y인 경우 2, 4사분면에는 K가 없으므로 1,3사분면 탐색
			result = find_K(A, u, u + x, l + y, r, K, result) # 1사분면
			result = find_K(A, u + y, d, l, l + x, K, result) # 3사분면
		
		if A[u+y][l+x] == K: #(x, y)의 값이 K와 같으면 해당 좌표 result에 저장
			result = (u+y,l+x)
			
		return result # 결과 return 


n, K = map(int,input().split()) # n, K 입력
matrix = [] # 2차원 배열 생성
for _ in range(n): # 2차원 배열 입력받아서 저장
	matrix.append(list(map(int, input().split())))

result = (-1, -1) # result 초기화
print(find_K(matrix, 0, n-1, 0, n-1, K, result))

# find_K의 실행 시간을 T(n)이라고 했을 때, T(n)<=3T(n/2)+c가 된다. 
# 사분면으로 나누었을 때 x,y에 값이 없다면 각 사분면을 최대 3개 탐색하기 때문이다. 
# n=2^k이고 T(1)=c일 때, T(n) = 3T(n/2)+c = 3^2T(n/4)+c((3/2)+1) = 3^k*T(n/2^k)+c(1+(3/2)+...+(3/2)^(k-1)) = 3^k+2c((3^k)-1) 이 된다. 
# 따라서 수행시간을 Big-O로 표현하면 O(3^k) = O(3^(log2(n)) = O(n^log2(3))이 된다.