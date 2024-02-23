import sys

def dfs(visited, graph, start): 
    if start not in visited:
        visited.add(start)
        for neighbour in graph[start]:
            dfs(visited, graph, neighbour)
    return visited

file = sys.argv[1]
start = sys.argv[2]

f = open(file, 'r', encoding = "UTF-8")

verteces = []
pairs = []
while True:
    s = f.readline().strip('\n')
    if s == '':
        break
    else:
        vertex, city = [x for x in s.split('\t')]
        pairs.append([vertex, city])

f.close()


graph = dict()
for city in pairs:
    if city[0] in graph and city[1] in graph:
        graph[city[0]].update([city[1]])
        graph[city[1]].update([city[0]])
    elif city[0] in graph and city[1] not in graph:
        graph[city[0]].update([city[1]])
        graph[city[1]] = set([city[0]])
    elif city[0] not in graph and city[1] in graph:
        graph[city[1]].update([city[0]])
        graph[city[0]] = set([city[1]])
    elif city[0] not in graph and city[1] not in graph:
        graph[city[0]] = set([city[1]])
        graph[city[1]] = set([city[0]])


visited = set()
print(dfs(visited, graph, start))