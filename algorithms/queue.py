from collections import deque
import time, random
start = time.time()

def create_queue():
	queue = deque()
	return queue

def is_empty(queue):
	return len(queue) == 0

def enqueue(queue, item):
	queue.append(item)

def dequeue(queue):
	if is_empty(queue):
		return 'error'
	else:
		return queue.popleft()

def peek(queue):
	return queue[0]

queue = create_queue()

for i in range(100000):
	enqueue(queue, random.random())

while queue:
	dequeue(queue)

end = time.time()
print(end - start)
print(len(queue))