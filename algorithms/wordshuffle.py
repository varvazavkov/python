import sys, random

def shuffle(str1):

	a = list(str1)

	n = len(a)
	frst = [a[0]]
	lst = a[n - 1]

	a.pop(0)
	a.pop(n - 2)

	random.shuffle(a)

	for elem in a:
		frst.append(elem)

	frst.append(lst)

	return ''.join(frst)

print(' '.join([shuffle(x) for x in sys.argv[1].split(" ")]))