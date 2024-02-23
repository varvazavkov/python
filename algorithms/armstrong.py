import sys

def isArmstrong(n):

	masDig = [int(x) for x in str(n)]
	k = len(masDig)
	sumk = 0

	for elem in masDig:
		sumk += elem**k 

	if n == sumk:

		return 1

	else:

		return 0

n = int(sys.argv[1])

masNum = [x for x in range(1, n + 1)]
result = []

for elem in masNum:
	
	if isArmstrong(elem) == 1:
		result.append(elem)

print(result)
