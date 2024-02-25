'''
1. get_token_list(expr)
expr은 문자열로 수식을 나타냄
expr을 연산자와 피연산자로 나눈 후, 리스트에 담아 리턴함
*연산자는 +, -, *, /, ^ 5가지만 다루고, 연산자와 피연산자 사이에 공백이 올 수도 있음
*한 자리 이상의 실수가 등장할 수도 있음

2.infix_to_postfix(token_list)
token_list는 수식의 연산자와 피연산자가 infix 수식의 순서대로 저장된 리스트임
token_list를 postfix 수식으로 변환하고 그 결과를 리스트에 담아 리턴함

3.compute_postfix(token_list)
postfix 형식인 token_list에 대한 계산 값을 리턴함
*계산하기 전에 피연산자는 float으로 변환한 후 계산함
'''

class Stack:
    def __init__(self):
        self.items=[]
    def push(self, val):
        self.items.append(val)
    def pop(self):
        return self.items.pop()
    def top(self):
        if len(self.items)==0:
            return None
        return self.items[-1]
    def len_stack(self):
        return len(self.items)


def get_token_list(expr):
    expr=expr.replace(' ', '')
    token_list=[]
    i=0
    while i<len(expr):
        if expr[i].isdigit() or expr[i]=='.':
            j = i
            while j<len(expr) and (expr[j].isdigit() or expr[j]=='.'):
                j+=1
            token_list.append(expr[i:j])
            i=j
        elif expr[i] in '+-*/^':
            token_list.append(expr[i])
            i+=1
        elif expr[i]=='(':
            token_list.append(expr[i])
            i+=1
        elif expr[i]==')':
            token_list.append(expr[i])
            i+=1
        else:
            raise ValueError('Invalid character in input')
    return token_list


def infix_to_postfix(token_list):
    opstack=Stack()
    outstack=[]
    precedence={'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    for i in token_list:
        if i.isdigit() or '.' in i:
            outstack.append(float(i))
        elif i in '+-*/^':
            while (opstack.top() in precedence and precedence[opstack.top()] >= precedence[i]):
                outstack.append(opstack.pop())
            opstack.push(i)
        elif i=='(':
            opstack.push(i)
        elif i==')':
            while opstack.top()!='(':
                outstack.append(opstack.pop())
            opstack.pop()
    while opstack.top()!=None:
        outstack.append(opstack.pop())
    return outstack


def compute_postfix(token_list):
    value=Stack()
    for i in token_list:
        if isinstance(i, float):
            value.push(i)
        else:
            operand2 = value.pop()
            operand1 = value.pop()
            if i=='+':
                value.push(operand1 + operand2)
            elif i=='-':
                value.push(operand1 - operand2)
            elif i=='*':
                value.push(operand1 * operand2)
            elif i=='/':
                value.push(operand1 / operand2)
            elif i=='^':
                value.push(operand1 ** operand2)
    return value.pop()


expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)
