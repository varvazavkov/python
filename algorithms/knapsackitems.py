import sys, time

def memtable(value, weight, W):
	n = len(value)
	table = [[0 for a in range(W+1)] for i in range(n+1)]

	for i in range(n+1):
		for a in range(W+1):
			if i == 0 or a == 0:
				table[i][a] = 0

			elif weight[i-1] <= a:
				table[i][a] = max(value[i-1] + table[i-1][a-weight[i-1]], table[i-1][a])

			else:
				table[i][a] = table[i-1][a]       
	return table, value, weight


def knapsack_bottomup(value, weight, W):
	V, value, weight = memtable(value, weight, W)
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
			items_list.append([value[i-1], weight[i-1]])
			summ += value[i-1]
			res -= value[i-1]   
			a -= weight[i-1]  
	print(summ)
	return items_list
	


file = sys.argv[1] #'D:/items.txt'
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


print(knapsack_bottomup(value, weight, W))