graph = {
		'A': {'B':2, 'C':4},
		'B': {'C':3, 'D':1},
		'C': {'D':4},
		'D': {}
}

def dijkstrasAlgo(start, end, graph, path=[]):
	#print(start)
	path = path + [start]
	if start == end:
		return path
	if start not in graph:
		return path
	minDistance = min(list(graph[start].values()))
	minNode = list(graph[start].keys())[list(graph[start].values()).index(minDistance)]
	newpath = dijkstrasAlgo(minNode, end, graph, path)
	return newpath
	
print(dijkstrasAlgo('A', 'D', graph))