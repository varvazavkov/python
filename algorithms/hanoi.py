import sys

n = int(sys.argv[1])

def hanoi(n, fr, to, aux):
	if (n == 1):
		return [(fr, to)]
	else:
		return hanoi(n -1, fr, aux, to) + [(fr, to)] + hanoi(n - 1, aux, to, fr)

h = hanoi(n, 1, 2, 3)
print(h)