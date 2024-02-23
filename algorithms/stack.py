import time, random

start = time.time()

def create_stack():
	stack = []
	return stack

def is_empty(stack):
	return len(stack) == 0

def push(stack, item):
	stack.append(item)

def pop(stack):
	if is_empty(stack):
		return 'error'
	else:
		return stack.pop()

def peek(stack):
	return stack[-1]

stack = create_stack()

for i in range(100000):
	push(stack, random.random())

while stack:
	pop(stack)

end = time.time()
print(end - start)
print(len(stack))