import json
from pprint import pprint

def makeMetroGraph(originalFile, newFile):
	with open(originalFile) as data_file:    
	    data = json.load(data_file)


	liz_of_stations = data["stations"]
	newGraph = {}

	for stations in enumerate(liz_of_stations):
		
		key = stations[1]['name']
		value = stations[1]['neighbours']
		newGraph[key] = value

	##with open(newFile, 'w') as outfile:
	#    json.dump(newGraph, outfile, sort_keys = True, indent = 4,
	#ensure_ascii=False)

	return newGraph


graph = makeMetroGraph("brussels_metro_v2.json", "new_metro.json")


def BFS_path(graph, start, goal):
	#print "ENTER HERE "
	queue = [(start, graph[start])]
	nodes_visited = []
	nodes_visited.append(start)
	prev = {}
	prev[start] = None

	while queue:
		(vertex, path) = queue.pop(0)
		for node in path:
			if node["name"] not in nodes_visited:
				prev[node["name"]] = vertex
				if node["name"] == goal:
					nodes_visited.append(node["name"])
					return prev
				else:
					nodes_visited.append(node["name"])
					queue.append((node["name"], graph[node["name"]]))
			
	return prev


resultListBFS = BFS_path(graph, "Gare du Nord", "Roi Baudouin")

def pathReportingBFS(prev, start, goal):
	path = []
	currentV = goal
	
	while prev[currentV] != None:
		path.append(currentV)	
		currentV = prev[currentV]
	path.append(start)
	path.reverse()
	return path

path = pathReportingBFS(resultListBFS, "Gare du Nord", "Roi Baudouin")


def DFS_path(graph, start, goal):
	stack = [(start, graph[start])]

	nodes_visited = []
	prev = {}
	prev[start] = None

	counter = 0
	while stack:
		(vertex, path) = stack.pop()
		v = str(vertex)
		if v not in nodes_visited:
			nodes_visited.append(str(vertex))
			for node in path:
				if prev[vertex] != node["name"] and node["name"] not in prev.values():
					prev[node["name"]] = vertex
				if node["name"] == goal:
					nodes_visited.append(node["name"])
					return prev, nodes_visited 
				else:
					stack.append((node["name"], graph[node["name"]]))
			
	return prev, nodes_visited 

(resultListDFS, visited) = DFS_path(graph, "Gare du Nord", "Roi Baudouin")
#resultListDFS.reverse()

#pprint(resultListDFS)	
print len(resultListDFS)

def pathReportingDFS(prev, start, goal):
	path = []
	currentV = goal
	while prev[currentV] != None:
		path.append(currentV)	
		currentV = prev[currentV]
	path.append(start)
	path.reverse()
	return path

#print pathReportingDFS(resultListDFS, "Gare du Nord", "Roi Baudouin")

def IDDFS(graph, start, goal, limit):
	for depth in  range(0, limit):
		(resultList, visitedNodes) = DeepeningDFS(graph, start, goal, depth)
		if resultList != None:
			return resultList, visitedNodes
	
	return {}, visitedNodes

"""
def DLS(graph, node, goal, depth):
	if depth == 0 and node == goal:
		return node
	elif depth > 0:
		neighbours = graph[node]
		for child in neighbours:	
			found = DLS(graph, child["name"], goal, depth -1)
			if found != None:
				return found
	return None
"""

def DeepeningDFS(graph, start, goal, depth):
	stack = [(start, graph[start])]
	prev = {}
	prev[start] = None
	visited_nodes = []
	visited_nodes.append(start)
	while stack:
		(vertex, neighbours) = stack.pop()
		if depth > 0:
			for child in neighbours:
				if child["name"] not in visited_nodes:
					visited_nodes.append(child["name"])
					if prev[vertex] != child["name"] and child["name"] not in prev.values():
						prev[child["name"]] = vertex
					if child["name"] == goal:
						visited_nodes.append(child["name"])
						return prev, visited_nodes
					stack.append((child["name"], graph[child["name"]]))
			depth = depth - 1
	return None, visited_nodes

(resultList, l) = IDDFS(graph, "Gare du Nord", "Roi Baudouin", 3)


