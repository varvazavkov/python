import sys, random, copy, time

if len(sys.argv) == 1:
	n = 10
	out = False
elif len(sys.argv) == 2:
	n = int(sys.argv[1])
	out = False
else:
	n = int(sys.argv[1])
	out = sys.argv[2]

def rand_lst(n = 10):
	lst = [random.randint(1, 1000) for _ in range(1, n + 1)]
	return lst


def python_sort(lst, out = False):
	print('\npython sort') 
	arr = copy.deepcopy(lst)
	t0 = time.time()
	arr.sort()

	print(time.time() - t0)
	if out:
		print(arr)


def bubble_sort(lst, out = False):
	print('\nbubble sort')
	arr = copy.deepcopy(lst)
	t0 = time.time()

	for i in range(n - 1):
		for j in range(i + 1, n):
			if arr[i] > arr[j]:
				arr[i], arr[j] = arr[j], arr[i]
	print(time.time() - t0)
	if out:
		print(arr)


def insertion_sort(lst, out = False):
	print('\ninsertion sort')
	arr = copy.deepcopy(lst)
	t0 = time.time()

	for i in range(n):
		j = i
		while (j > 0) and (arr[j - 1] > arr[j]):
			tmp = arr[j - 1]
			arr[j - 1] = arr[j]
			arr[j] = tmp
			j -= 1

	print(time.time() - t0)
	if out:
		print(arr)


def selection_sort(lst, out = False):
	print('\nselection sort')
	arr = copy.deepcopy(lst)
	t0 = time.time()

	for i in range(n - 1):
		for j in range(i + 1, n):
			if arr[j] < arr[i]:
				arr[i], arr[j] = arr[j], arr[i]

	print(time.time() - t0)
	if out:
		print(arr)


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

def merge_s(arr):
	if len(arr) == 1:
		return arr
	else:
		mid = len(arr) // 2
		left = merge_s(arr[:mid])
		right = merge_s(arr[mid:])
		return merge(left, right)

def merge_sort(lst, out = False):
	print('\nmerge sort')
	t0 = time.time()
	res = copy.deepcopy(lst)
	arr = merge_s(res)
	print(time.time() - t0)
	if out:
		print(arr)


def partition(l, r, nums):
	pivot, ptr = nums[r], l
	for i in range(l, r):
		if nums[i] <= pivot:
			nums[i], nums[ptr] = nums[ptr], nums[i]
			ptr += 1
	nums[ptr], nums[r] = nums[r], nums[ptr]
	return ptr

def quicksort(l, r, nums):
	if len(nums) == 1:  
		return nums
	if l < r:
		pi = partition(l, r, nums)
		quicksort(l, pi-1, nums)  
		quicksort(pi+1, r, nums)  
	return nums


def quick_sort(lst, out = False):
	print('\nquick sort')
	t0 = time.time()
	res = copy.deepcopy(lst)
	arr = quicksort(0, len(res) - 1,res)
	print(time.time() - t0)
	if out:
		print(arr)


lst = rand_lst(n)
bubble_sort(lst, out)
insertion_sort(lst, out)
selection_sort(lst, out)
quick_sort(lst, out)
merge_sort(lst, out)
python_sort(lst, out)
