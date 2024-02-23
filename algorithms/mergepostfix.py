import sys

def merge(left, right):
	s = ''
	i = -1
	left = ''.join(left)
	right = ''.join(right)

	if len(left) < len(right):
		rng = len(left)
	else:
		rng = len(right)

	while abs(i) <= rng:
		if left[i] == right[i]:
			s += left[i]
			i -= 1
		else:
			break
	str1 = [s[::-1]]
	return str1


def merge_sort(arr):
	if len(arr) == 1:
		return arr
	else:
		mid = len(arr) // 2
		left = merge_sort(arr[:mid])
		right = merge_sort(arr[mid:])
		return merge(left, right)


s = sys.argv[1]
s = s.split(' ')
substr = merge_sort(s)
substr = ''.join(substr[::-1])

print(substr)