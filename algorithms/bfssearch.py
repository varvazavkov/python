import sys
from collections import deque

def distance(graph, start, end):
	vert = deque([start])
	visited = set([start])
	dist = {x: -1 for x in graph.keys()}
	dist[start] = 0

	while vert:
		vertex = vert.popleft()
		for neigh in graph[vertex]:
			if neigh not in visited:
				vert.append(neigh)
				visited.add(neigh)
				dist[neigh] = dist[vertex] + 1
		if end in visited:
			break

	if end in visited:
		return dist[end] #visited, dist
	else:
		return -1

file = sys.argv[1]
actor1 = sys.argv[2]
actor2 = sys.argv[3]

actors = {}
movies = {}

f = open(file, 'r')
# D:/actors.tsv

while True:
	s = f.readline().strip('\n')
	if s == '':
		break
	else:
		actor, movie = [x for x in s.split('\t')]
		if actor not in actors:
			actors[actor] = set([movie])
		else:
			actors[actor].add(movie) 
		if movie not in movies:
			movies[movie] = set([actor])
		else:
			movies[movie].add(actor) 
f.close()

graph = {}

for actor in actors:
	tmp = set()
	for mov in actors[actor]:
		tmp.update(movies[mov])
	graph[actor] = tmp - set([actor])

print(distance(graph, actor1,actor2))