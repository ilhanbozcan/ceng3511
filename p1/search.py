import os
import sys

graph = {}
file = sys.argv[1]
file_path = os.path.abspath(file)
f = open(file_path, "r")

####################################### TXT to GRAPH with no cost #################################

def TxtToGraph(path):
    for i in f:
        tmp = {}
        a = 3
        b = 5
        while(a<len(i) and b<len(i)):
            tmp[i[a]] = int(i[b][0])
            a = a+5
            b = b+5
            graph[i[0]] = tmp
    return graph

graph =  TxtToGraph(f)
"""Here with cost"""

no_cost_graph = {}
cost_graph = {}

for key,value in graph.items():
    tmp = []
    tmp_no_cost = {}
    for a,b in value.items():

        if (b != 0):
            tmp.append(a)
            tmp_no_cost[a] = int(b)
    no_cost_graph[key] = tmp
    cost_graph[key] = tmp_no_cost
#print(cost_graph)
#print(no_cost_graph)


##############################  BFS #################################
def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

#################################### DFS ##########################################################


def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))

#########################################  UCS ###########################

def ucs(graph,start,end,visited=[],distances={},predecessors={}):

    if start == end:
        path=[]
        while end != None:
            path.append(end)
            end=predecessors.get(end,None)
        return path[::-1]

    if not visited:
        distances[start] = 0
    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor,sys.maxsize)

            tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor] = start
    visited.append(start)
    unvisiteds = dict((k, distances.get(k,sys.maxsize)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)
    return ucs(graph,closestnode,end,visited,distances,predecessors)

################################################################
start = input("Please enter the start state : ")
end = input("Please enter the end state : ")

bfs_result = bfs(no_cost_graph,start,end)
dfs_result = dfs(no_cost_graph,start,end)
ucs_result = ucs(cost_graph,start,end)

seperate = " - "
bfs_list = []
dfs_list = []
ucs_list = []
for i in bfs_result:
    bfs_list.append(str(i))

print("BFS : ", end="")
print(seperate.join(bfs_list))



for i in dfs_result:
    dfs_list.append(str(i))

print("DFS : ", end="")
print(seperate.join(dfs_list))


for i in ucs_result:
    ucs_list.append(str(i))

print("UCS : ", end="")
print(seperate.join(ucs_list))
