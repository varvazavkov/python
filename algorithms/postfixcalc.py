import sys

def create_stack():
	stack = []
	return stack

def push(stack, item):
	stack.append(item)

def pop(stack):
	if is_empty(stack):
		return 'is empty'
	else:
		return stack.pop()

def is_empty(stack):
	return len(stack) == 0

def top(mas):
	stack = create_stack()
	for elem in mas:
		push(stack, elem)
	return stack

def norm_write(a, b, oper):
	if oper == '+':
		return a + b
	if oper == '-':
		return a - b
	if oper == '*':
		return a * b
	if oper == '/':
		return a / b

def calculate(expr):
	oper = ['+', '-', '*', '/']
	res = create_stack()

	for elem in expr:
		if elem == ' ':
			continue
		else:
			if elem in oper:
				if not is_empty(res):
					b = pop(res)
					if not is_empty(res):
						a = pop(res)
						push(res, norm_write(a, b, elem))
					else:
						return 'invalid input' 
				else:
					return 'invalid input'
			else:
				push(res, int(elem))
	return res[0]

expr = sys.argv[1]
expr = expr.split(' ')
print(calculate(expr))