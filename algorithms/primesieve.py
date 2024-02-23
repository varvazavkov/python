import sys

n = int(sys.argv[1])

if len(str(n)) == 1:
    n = 10

num = n + 1
a = 1

mas = [x for x in range(2, num)]

for elem in mas:
    for dig in mas:
        if elem != dig:
            if dig % elem == 0:
                mas.remove(dig)
    

print(mas)