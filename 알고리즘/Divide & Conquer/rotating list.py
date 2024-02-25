def find_min_idx(A):
    for i in range(1, len(A)):
		if A[i-1] > A[i]:
			return i
	return len(A)

A = list(map(int,input().split()))
print(len(A) - find_min_idx(A))

# 만약 n개의 숫자 중 k번의 회전을 했다면 원래 리스트의 첫 번째 요소는 (n-k+1)번째에 위치하게 된다. 
# 원래 리스트의 첫 번재 요소는 최솟값이므로 입력된 리스트에서 최솟값이 몇 번째에 위치한지 알면 회전 횟수를 알 수 있다.
# 최솟값이 어디에 위치한지 비교하기 위해서는 최대 n번의 비교만 하면 되므로 Big-O 표기를 하면 O(n)의 수행 시간이 소요된다.