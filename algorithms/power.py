import sys

def power(a, n):
	if n == 0:
		return 1
	if n == 1:
		return a
	if n % 2 == 0:
		return power(a*a, n // 2)
	else:
		return power(a*a, n // 2) * a
	
a = int(sys.argv[1])
n = int(sys.argv[2])

print(power(a,n))