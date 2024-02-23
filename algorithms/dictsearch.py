import sys, time

f = open(sys.argv[1],'r')

word = sys.argv[2]

lines = f.readlines()
l_w = len(word)

start0 = time.time()
res = []

lines = ''.join(lines).split('\n')
for line in lines:
	if word == line[:l_w]:
		res.append(line)
print(res)
end = time.time()
print(end - start0)

start0 = time.time()

def find_word(lines, word):
	first = 0
	last = len(lines) - 1
	res = []

	while first <= last:
		guess = int(first + (last - first)*0.5)
		midpoint = lines[guess]
		if lines[guess - 1] < word <= lines[guess]:
			res.append(midpoint)
			return guess
		elif midpoint > word:
			last = guess
			guess = int(first + (last - first)*0.5)
		else:
			first = guess
			guess = int(first + (last - first)*0.5)			
	return res

ind = find_word(lines, word)
res = []

if ind != []:
	for line in lines[ind:]:
		if word == line[:l_w]:
			res.append(line)
		else:
			break
	print(res)
else:
	print(ind)

end = time.time()
print(end - start0)

f.close()