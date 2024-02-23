import sys

n = int(sys.argv[1])
num = n
result = [num]

while num > 1:
	if (num % 2 == 0):
		num = num//2
		result.append(num)
	else:
		num = 3*num + 1
		result.append(num)

lng = len(result)

maxm = result[0]

for elem in result:
	if elem > maxm:
		maxm = elem

print('len:', lng, ' max:', maxm, result)

