import sys

n = int(sys.argv[1])

size = 2**n

h = [[0]*n for i in range(size)]
ind = size//2

for i in range(ind):
		h[i][0] = 1

index = ind//2

j = 1
num = 1

while index > 0:

	for i in range(index):
		h[i][j] = 1

		for k in range(2**num):
			h[i + k*(index*2)][j] = 1 
			
	num += 1
	j += 1
	index = index//2

for i in range(size):
	s = str(h[i]) + '\n'
	print(s)