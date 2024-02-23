import sys

n = int(sys.argv[1])

result = []

for i in range(n+1):
        result.append([])

i = 1

result[0].append(1)

for i in range(1, n + 1):

    result[i].append(1)

    for j in range(1, i):
            k = result[i-1][j-1] + result[i-1][j]
            result[i].append(k)
    result[i].append(1)


print(result)