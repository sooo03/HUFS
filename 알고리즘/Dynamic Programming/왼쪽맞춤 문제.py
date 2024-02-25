W = int(input())
words = input().split()
# code below

dp = [0]*len(words)
dp[0] = (W-len(words[0]))**3

for i in range(1,len(words)):
	currWidth = 0
	minPenalty = len(words)*(W**3)
	j = i
	while j>=0:
		currWidth += len(words[j]) + 1
		if j == 0:
			currPenalty = (W-currWidth+1)**3
		else:
			currPenalty = dp[j-1]+ (W-currWidth+1)**3	
		if currWidth-1 <= W:
			if minPenalty > currPenalty:
				minPenalty = currPenalty
		else:
			break
		j = j-1
  
	dp[i] = minPenalty
 
print(dp[len(words)-1])

'''
dp 테이블을 만들어주고 처음 문자의 penalty 값을 dp[0]에 저장해준다.
j에 i값을 대입하고, 0보다 클 동안 제일 작은 penalty 값을 찾아서 테이블에 저장한다.
while문을 돌때마다 현재 길이를 증가시켜주고 현재 penalty 값을 업데이트 시켜준다.
이때 j가 1이면 현재 penalty 값만 바뀌고 0이 아니라면
테이블에 저장되어 있는 하나 앞의 값을 가져와서 저장해준다.
현재 넓이가 폭보다 작거나 같고 penalty 최소값보다 현재 값이 작으면 minPenalty에 저장해준다.
while문을 빠져나오면 dp[i]에 minPenalty값을 저장해준다.
dp[i] = min(dp[j])+(j+1)번째부터 i번째까지 마지막줄에 오는 penalty 값)이고
수행시간은 O(n^2)이다.
'''