def LPS(X):
    	n = len(X)
	dp = [[0]*n for i in range(n)]
	
	#길이가 1인 경우
	for i in range(n):
		for j in range(n):
			dp[i][j] = 1
		
	for k in range(2, n+1): #부분 문자열의 길이(k)를 반복
		for i in range(n-k+1): #부분 문자열의 시작 인덱스를 반복
			j = i+k-1
			if X[i]==X[j]: #양 끝점이 같을 때
				if k==2: #길이가 2인 경우
					dp[i][j] = 2
				else:
					dp[i][j] = dp[i+1][j-1] + 2
			else: #양 끝점이 다를 경우
				dp[i][j] = max(dp[i][j-1], dp[i+1][j])
	return dp[0][n-1]

word = input()
ans = LPS(word)
print(ans)

# 이중 for문을 사용하여 외부 for문에서 
# 부분 문자열의 길이를 반복하고 내부 for문에서는 
# 부분 문자열의 시작 인덱스를 반복하여서 수행시간은 O(n^2)이 된다.