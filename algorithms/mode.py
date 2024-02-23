import sys

mas = [int(x) for x in sys.argv[1].split(",")]

result = []


for elem in mas:
	found = False
	for val in result:
		if val[0] == elem:
			val[1] += 1
			found = True
			break
	if not found:
		result += [[elem, 1]]

res = []
maxi = 1

for i in range(len(result)):
	if result[i][1] > maxi:
		maxi = result[i][1]
		

for i in range(len(result)):
	if maxi != 1:
		if result[i][1] == maxi:
			res.append(result[i][0])

print(res)