import sys, math

def haar(n):
	matr = [[0] * n for i in range(n)]
	k = n

	for i in range(n):
		matr[0][i] = 1/math.sqrt(n)

	num = n//2

	matr[1][:num] = matr[0][:num]

	for i in range(num, n):
		matr[1][i] = -1/math.sqrt(n)


	den = math.sqrt(2)
	res = matr[1]
	k = n

	for j in range(2, num + 1):
		if math.log2(j) % 1 == 0:
			i = 0
			z = 0
			while z!= n:
				matr[j + i][z:k//2 + z] = res[k//4:3*k//4]
				matr[j + i] = [t*den for t in matr[j + i]]
				z +=len(res[:k//2])
				i += 1
			res = res[k//4:3*k//4]
			k = k//2
			den = den*math.sqrt(2)


	for i in range(n):
		for j in range(n):
			matr[i][j] = round(matr[i][j], 3)
	
	if math.log2(n) % 1 == 0:
		return matr
	else:
		print("Digit must be a power of two")



n = int(sys.argv[1])
matr = haar(n)

print(matr)