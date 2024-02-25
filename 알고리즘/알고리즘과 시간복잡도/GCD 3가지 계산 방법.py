def gcd_sub(a, b):
    while a*b!=0:
		if a>=b:
			a=a-b
		else:
			b=b-a
	return a+b

def gcd_mod(a, b):
	while a*b!=0:
		if a>=b:
			a=a%b
		else:
			b=b%a
	return a+b
			
def gcd_rec(a, b):
	if a*b==0:
		return a+b
	elif a>=b:
		return gcd_rec(a%b,b)
	else:
		return gcd_rec(a,b%a)
	
# a, b를 입력받는다
a,b=map(int,input().split())
# gcd_sub, gcd_mod, gcd_rec을 각각 호출하여, x, y, z에 리턴값을 저장한다
x=gcd_sub(a,b)
y=gcd_mod(a,b)
z=gcd_rec(a,b)
print(x, y, z)
