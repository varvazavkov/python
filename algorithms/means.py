import sys

mas = [int(x) for x in sys.argv[1].split(",")]


gm = 1

for elem in mas:
	if elem == 0:
		gm = 0
		break
	else:
		gm *= elem**(1/len(mas))



arifm = 0

for elem in mas:
	arifm += elem

arifm = arifm/(len(mas))



if len(mas)%2 != 0:
	ind = len(mas)//2
	med = mas[ind]

if len(mas)%2 == 0:
	ind1 = len(mas)//2
	ind2 = len(mas)//2 - 1
	med = (mas[ind1] + mas[ind2])/2


summ = 0

for el in mas:
	summ += el**2

qvdr = (summ/len(mas))**(1/2)


result = [gm, arifm, med, qvdr]

for i in range(len(result)):
	result[i] = round(result[i], 2)


print(result)