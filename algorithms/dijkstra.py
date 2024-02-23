import math, sys

file = sys.argv[1]
start = sys.argv[2]

def dijkstra(graph, vertex):
    visited = set()
    distance = {key: math.inf for key in graph}
    distance[vertex] = 0
    while len(visited) < len(graph):
        cur = sorted([elem for elem in list(distance.items()) if elem[1] != math.inf and elem[0] not in visited], key = lambda x: x[1])[0][0]
        for val in graph[cur]:
            if val[0] in visited:
                continue
            if distance[val[0]] == math.inf:
                distance[val[0]] = distance[cur] + val[1]
            elif distance[cur] + val[1] < distance[val[0]]:
                distance[val[0]] = distance[cur] + val[1]
        visited.add(cur)
    return distance

f = open(file, 'r', encoding = "UTF-8")


pairs = []
while True:
    s = f.readline().strip('\n')
    if s == '':
        break
    else:
        vertex, city, dist = [x for x in s.split('\t')]
        pairs.append([vertex, city, dist])

f.close()


graph = dict()
for city in pairs:
    if city[0] in graph and city[1] in graph:
        graph[city[0]].append((city[1], int(city[2])))
        graph[city[1]].append((city[0], int(city[2])))
    elif city[0] in graph and city[1] not in graph:
        graph[city[0]].append((city[1], int(city[2])))
        graph[city[1]] = list([(city[0], int(city[2]))])
    elif city[0] not in graph and city[1] in graph:
        graph[city[1]].append((city[0], int(city[2])))
        graph[city[0]] = list([(city[1], int(city[2]))])
    elif city[0] not in graph and city[1] not in graph:
        graph[city[0]] = list([(city[1], int(city[2]))])
        graph[city[1]] = list([(city[0], int(city[2]))])

distances = sorted(dijkstra(graph, start).items(), key = lambda x: x[1])

for i in range(10):
    if i < 5:
        if i == 0:
            print('Top 5 nearest cities:')
        print(distances[i+1])
    else:
        if i == 5:
            print('Top 5 distant cities:')
        print(distances[-(10-i)])