import sys
import matplotlib.pyplot as plt

def replace(str1):
    res = ""
    for c in str1:
        if c == "L":
            res += "+RF-LFL-FR+"
        elif c == "R":
            res += "-LF+RFR+FL-"
        else:
            res += c
    return res

def fin(str1):
    res = ""
    for c in str1:
        if c != "L" and c != "R":
            res += c
    return res

def fin_points(str1):
	rdict = {(0, 1): (1, 0),(1, 0): (0,-1),(0,-1): (-1,0),(-1,0): (0,1)} 
	ldict = {(1, 0): (0, 1),(0,-1): (1, 0),(-1,0): (0,-1),(0, 1): (-1,0)}
	points = [(0, 0)]
	vect = (1, 0)

	for c in str1:
		if c == "+":
			vect = ldict[vect]
		elif c == "-":
			vect = rdict[vect]
		elif c == "F":
			tuple0 = list(vect)[0] + list(points[-1])[0]
			tuple1 = list(vect)[1] + list(points[-1])[1]
			points.append((tuple0, tuple1))
	return points

n = int(sys.argv[1])

str1 = 'L'
for i in range(n):
	str1 = replace(str1)

seq3 = fin_points(fin(str1))
plt.plot([p[0] for p in seq3], [p[1] for p in seq3])
plt.show()
