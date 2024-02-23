import sys

def countStr(str1, str2):

	st1 = str1.lower()
	st2 = str2.lower()

	lng = len(st2)
	length = len(st1)

	count = 0

	for i in range(length):

		if st1[i:(lng + i)] == st2:

			count += 1

	return count



str1 = str(sys.argv[1])

str2 = str(sys.argv[2])

count = countStr(str1, str2)

print(count)