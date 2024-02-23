import sys

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

def check_brackets(bracket):
	stack = create_stack()

	for elem in bracket:
		if elem == '(':
			push(stack, elem)
		if elem == ')':
			if not stack:
				return 'False'
			else:
				pop(stack)
	if is_empty(stack):
		return 'True'
	else:
		return 'False'

bracket = sys.argv[1]
print(check_brackets(bracket))