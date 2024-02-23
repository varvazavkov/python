import sys, time

def greedy(v, w, W):
	print('\nGreedy knapsack')
	t0 = time.time()
	items = [[v[i]/w[i], v[i], w[i]] for i in range(len(v))]
	items = sorted(items, reverse = True)

	knapsack = {'value': 0, 'weight': 0, 'items': []}
	for item in items:
		_, value, weight = item
		if knapsack['weight'] + weight <= W:
			knapsack['value'] += value
			knapsack['weight'] += weight
			knapsack['items'].append([value, weight])
		if knapsack['weight'] == W:
			break
	print(knapsack['value'])
	print(time.time() - t0)
	return knapsack


def knapsack_topdown(value, weight, W, ind):
	if W <= 0 or ind < 0 or ind >= len(value):
		return 0
	elif weight[ind] <= W:
		value1 = value[ind] + knapsack_topdown(value, weight, W - weight[ind], ind + 1)
		value2 = knapsack_topdown(value, weight, W, ind + 1)
		return max(value1, value2)
	else:
		return 0


def get_memtable(value, weight, W):
	n = len(value)
	V = [[0 for a in range(W+1)] for i in range(n+1)]

	for i in range(n+1):
		for a in range(W+1):
			if i == 0 or a == 0:
				V[i][a] = 0

			elif weight[i-1] <= a:
				V[i][a] = max(value[i-1] + V[i-1][a-weight[i-1]], V[i-1][a])

			else:
				V[i][a] = V[i-1][a]       
	return V, value, weight


def knapsack_bottomup(value, weight, W):
	print('\nBottom-up knapsack')
	t0 = time.time()
	V, value, weight = get_memtable(value, weight, W)
	n = len(value)
	res = V[n][W]      
	a = W              
	items_list = []
	summ = 0    
    
	for i in range(n, 0, -1):  
		if res <= 0: 
			break
		if res == V[i-1][a]:  
			continue
		else:
			items_list.append([weight[i-1], value[i-1]])
			summ += value[i-1]
			res -= value[i-1]   
			a -= weight[i-1]  
	print(summ)
	print(time.time() - t0)
	return summ
	


file = sys.argv[1]
n = int(sys.argv[2])
W = int(sys.argv[3])

f = open(file,'r')
value = []
weight = []
while True:
	s = f.readline().strip('\n')
	if s == '':
		break
	else:
		v, w = [int(x) for x in s.split('\t')]
		value.append(v)
		weight.append(w)
f.close()

if n < len(value):
	value = value[:n]
	weight = weight[:n]




v = [ 20, 5, 10, 25, 15, 40]
w = [1, 2, 3, 4, 7, 8]
W1 = 10

greedy(value, weight, W)
t0 = time.time()
print('\nTop-down knapsack')
print(knapsack_topdown(value, weight, W, 0))
print(time.time() - t0)
knapsack_bottomup(value, weight, W)

# f(v, w, W)
