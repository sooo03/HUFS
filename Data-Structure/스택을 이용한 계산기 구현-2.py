def get_token_list(expr):
	expr = expr.replace(' ', '')
	ch = ''
	token_list = []
	for s in expr:
		if s in '+-*/^()':
			if ch != '':
				token_list.append(ch)
			token_list.append(s)
			ch = ''
		else:
			ch += s
	if ch != '':
		token_list.append(ch)
	return token_list
	
	
def infix_to_postfix(token_list):
	opstack = Stack()
	outstack = []
	prec = {'+':3, '-':3, '*':2, '/':2, '^':1, '(':4}
	for token in token_list:
		if (token in '+-*/^()') == False:
			outstack.append(token)
		elif token == '(':
			opstack.push(token)
		elif token == ')':
			while len(opstack) != 0:
				pop = opstack.pop()
				if pop == '(':
					break
				outstack.append(pop)
		elif token in '+-*/^':
			while len(opstack) != 0:
				if prec[token] >= prec[opstack.top()]:   # 자신보다 우선순위가 높거나 같은 연산자는 차례대로 pop
					outstack.append(opstack.pop())
				else:
					break
			opstack.push(token)
				
	while len(opstack) != 0:
		outstack.append(opstack.pop())
	return outstack
	
def compute_postfix(token_list):
	numbers = Stack()
	result = 0
	for token in token_list:
		if token in '+-*/^':
			b, a = numbers.pop(), numbers.pop()
			if token == '+':
				numbers.push(a + b)
			elif token == '-':
				numbers.push(a - b)
			elif token == '*':
				numbers.push(a * b)
			elif token == '/':
				numbers.push(a / b)
			elif token == '^':
				numbers.push(a ** b)
		else:
			numbers.push(float(token))
	return numbers.pop()
