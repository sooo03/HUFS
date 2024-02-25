import heapq

def solve(F):
	H = []
	F = sorted(F)
	for i in range(len(F)):
		heapq.heappush(H, (F[i], str(i)))
	while len(H) > 1:
		a = heapq.heappop(H)
		b = heapq.heappop(H)
		heapq.heappush(H, (a[0]+b[0], '('+a[1]+' '+b[1]+')'))
	a = heapq.heappop(H)
	heapq.heappush(H, a[1])
	expr = H.pop()
	temp = 0
	t =''
	ans = []
	for i in expr:
		if i == '(':
			if t != '':
				ans.append(F[int(t)]*temp)
				t = ''
			temp += 1
		elif i == ')':
			if t != '':
				ans.append(F[int(t)]*temp)
				t = ''
			temp -= 1
		elif i == ' ':
			if t != '':
				ans.append(F[int(t)]*temp)
				t = ''
			continue
		else:
			t = t+i
	return sum(ans)

F = list(map(int, input().split()))
print(solve(F))