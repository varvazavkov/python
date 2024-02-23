import sys, math


def func(x):

        if (x == 0):

                return 1

        else:

                return math.atan(x) / x

a = float(sys.argv[1])

b = float(sys.argv[2])

n = int(sys.argv[3])


h = (b - a) / n


x = a 

s1 = 0

while (x < b ):

        s1 += (func(x) + func(x+h)) * h/2

        x += h


print(s1)