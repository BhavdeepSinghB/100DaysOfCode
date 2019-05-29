graph = {
		'A': ['B', 'C'],
		'B': ['C', 'D'],
		'C': ['D'],
		'D': []
	}


def findPath(start, end, graph, path=[]):
	path = path + [start]
	if(start == end):
		return path
	if start not in graph:
		return None
	for node in graph[start]:
		if node not in path:
			newpath = findPath(node, end, graph, path)
			if newpath: return newpath
	return None

def findPaths(start, end, graph, path=[]):
	#print(type(path))
	path = path + [start]
	if start == end:
		return [path]
	if not start in graph:
		return []
	paths = []
	for node in graph[start]:
		if node not in path:
			newpaths = findPaths(node, end, graph, path)
			for newpath in newpaths:
				paths.append(newpath)
	return paths
def findShortestPath(start, end, graph):
	paths = findPaths(start, end, graph)
	min = paths[0]
	for l in paths:
		if len(l) < len(min):
			min = l
	return min

print(findPaths('A', 'D', graph))
#print(findPath('A', 'D', graph))
print(findShortestPath('A', 'D', graph))