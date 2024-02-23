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

print(result)