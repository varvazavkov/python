import sys, random

n = int(sys.argv[1])

list1 = [random.randint(0, n) for _ in range(random.randrange(1, n+1))]
list2 = [random.randint(0, n) for _ in range(random.randrange(1, n+1))]

list1.sort()
list2.sort()
print(list1)
print(list2)

result = []
while (len(list1) and len(list2)):
	if list1[0] <= list2[0]:
		result.append(list1.pop(0))
	else:
		result.append(list2.pop(0))

print(result + list1 + list2)