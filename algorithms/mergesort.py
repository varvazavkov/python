import sys, time, random
start = time.time()

def merge(left, right):
	res = []
	i, j = 0, 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			res.append(left[i])
			i += 1
		else:
			res.append(right[j])
			j += 1
	while i < len(left):
		res.append(left[i])
		i += 1
	while j < len(right):
		res.append(right[j])
		j += 1
	return res

def merge_sort(arr):
	if len(arr) == 1:
		return arr
	else:
		mid = len(arr) // 2
		left = merge_sort(arr[:mid])
		right = merge_sort(arr[mid:])
		return merge(left, right)

n = int(sys.argv[1])
m = int(sys.argv[2])
k = int(sys.argv[3])

list1 = [random.randint(1, m) for _ in range(1, n + 1)]

res = merge_sort(list1)

end = time.time()
print(end - start)

if k:
	print(res[-k:])