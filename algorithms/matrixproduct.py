import sys

n = sys.argv

k = len(n)  #количество заданных матриц


def strToMatr(matr):
	matr = matr.split(',')
	matr = [c.split(' ') for c in matr]
	matr = [[float(c) for c in r if c != ' '] for r in matr]
	return matr


def mulMatr (mas1, mas2):

	cl = len(mas1[0])
	rw = len(mas2)

	if cl != rw:
		return 0

	if cl == rw:
		result = [[0]*len(mas2) for i in range(len(mas1))]

		for i in range(len(mas1)):
			for j in range(len(mas2[0])):
				s = 0
				for k in range(len(mas1[0])):
					s += mas1[i][k]*mas2[k][j]
				result[i][j] = s
		return result




masMatr = []

for i in range(1, k):
	matr = strToMatr(n[i])
	masMatr.append(matr)

res = 1
flag = 0

if k == 2:
	print(strToMatr(n[1]))


if k != 1:
	for i in range(1, k):
		if mulMatr(masMatr[i - 1], masMatr[i]) != 0:
			flag = 1
			res *= mulMatr(masMatr[i - 1], masMatr[i])
			i += 1
		else:
			print("Error: incompatible sizes of matrices")
			flag = 0
			break
	if flag != 0:
		print(res)
else: print("Error: no matrices")