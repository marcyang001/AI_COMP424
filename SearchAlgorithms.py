import json
from pprint import pprint

def makeMetroGraph(originalFile, newFile):
	with open(originalFile) as data_file:    
	    data = json.load(data_file)


	liz_of_stations = data["stations"]
	newGraph = {}
	newGraphWithCost = {}

	for stations in enumerate(liz_of_stations):
		key = stations[1]['name']
		value = stations[1]['neighbours']
		newGraph[key] = value
	
	
	for stations in enumerate(liz_of_stations):
		key = stations[1]['name']
		neighbours = stations[1]['neighbours']
		counter = 0
		for s in neighbours:
			if int(s['line']) >=4:
				stations[1]['neighbours'][counter]['cost'] = 1
			else:
				stations[1]['neighbours'][counter]['cost'] = 2	
			counter = counter + 1

		value = stations[1]['neighbours']
		newGraphWithCost[key] = value

	#with open(newFile, 'w') as outfile:
	#    json.dump(newGraphWithCost, outfile, sort_keys = True, indent = 4,
	#ensure_ascii=False)

	return newGraph, newGraphWithCost


(graph, graphwithCost) = makeMetroGraph("brussels_metro_v2.json", "new_metro.json")

#graph = makeMetroGraph("brussels_metro_v2.json", "new_metro_with_cost.json")



def pathReporting(prev, start, goal):
	path = []
	currentV = goal
	while prev[currentV] != None:
		path.append(currentV)	
		currentV = prev[currentV]
	path.append(start)
	path.reverse()
	return path

def BFS_path(graph, start, goal):
	
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




def IDDFS(graph, start, goal, limit):
	for depth in  range(0, limit+1):
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
	r_level = 0
	stack = [(start, graph[start], r_level)]
	prev = {}
	prev[start] = None
	visited_nodes = []
	visited_nodes.append(start)
	#print depth
	while stack:
		
		(vertex, neighbours, r_level) = stack.pop()
		if r_level >= depth:
			continue
		else:
			for child in neighbours:
				if child["name"] not in visited_nodes:
					visited_nodes.append(child["name"])
					if prev[vertex] != child["name"] and child["name"] not in prev.values():
						prev[child["name"]] = vertex
					if child["name"] == goal:
						visited_nodes.append(child["name"])
						return prev, visited_nodes
				
					stack.append((child["name"], graph[child["name"]], r_level+1))
		
	return None, visited_nodes

#(resultList, l) = IDDFS(graph, "Gare du Nord", "Roi Baudouin", 11)

"""
The uniform Cost Search implements BFS but chooses to visit the path with lowest cost first
"""
def UniformCostSearch(graphWithCost, start, goal):

	queue = [(start, graph[start], 0, None)]
	nodes_visited = {}
	nodes_visited[start] = 0
	prev = {}
	prev[(start, 0, None)] = None

	while queue:
		(vertex, path, cost, line) = queue.pop(0)

		path.sort()
		for node in path:
			
			if not nodes_visited.has_key(node["name"]):
				prev[(node["name"], node["cost"], node["line"])] = (vertex, cost, line)
				if node["name"] == goal:
					nodes_visited[node["name"]]= node["cost"]
					return prev
				else:
					nodes_visited[node["name"]]= node["cost"]
					queue.append((node["name"], graph[node["name"]], node["cost"], node["line"]))

	return prev, nodes_visited

def UFSPathReporting(prev, start, goal):
	path = []
	currentV = goal
	#find the node in the prev list
	#(station, cost, line) = None
	for k, v in prev.items():
		if k[0] == goal:
			(station, cost, line) = (k[0], k[1], k[2])
			break


	while prev[(station, cost, line)] != None:
		path.append((station, cost, line))	
		(station, cost, line) = prev[(station, cost, line)]
	path.append(start)
	path.reverse()
	return path





""" 
Question 1 a)

"""

print "SOLUTION WITH SAME TRANSITION COST (SAMPLE OUTPUT FROM DFS)"


(resultListDFS, visited) = DFS_path(graph, "Gare du Nord", "Roi Baudouin")

path = pathReporting(resultListDFS, "Gare du Nord", "Roi Baudouin")

pprint(pathReporting(resultListDFS, "Gare du Nord", "Roi Baudouin"))


# here is the BFS
#resultListBFS = BFS_path(graph, "Gare du Nord", "Roi Baudouin")
#path = pathReporting(resultListBFS, "Gare du Nord", "Roi Baudouin")
#pprint(pathReporting(resultListBFS, "Gare du Nord", "Roi Baudouin"))


print "\n\n"

"""
Question 1 b) 

"""
print "Solution with the lowest cost (sample output for uniform search cost)"

print "Print Format: station name, cost, metro line"

s = UniformCostSearch(graphwithCost, "Gare du Nord", "Roi Baudouin")


p = UFSPathReporting(s, "Gare du Nord", "Roi Baudouin")
pprint(p)







