def add_node(v):
    if v in graph:
        print(v,"is already present in graph")
    else:
        graph[v]=[]
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"not present in graph")
    elif v2 not in graph:
        print(v2,"not present in graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
graph={}
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
add_node("5")
add_node("3")
add_node("4")
add_node("7")
add_node("2")
add_node("8")
add_edge("5","3")
add_edge("5","7")
add_edge("3","2")
add_edge("3","4")
add_edge("7","4")
add_edge("4","8")
print(graph)
print("Breadth first search is : ")
print(bfs(visited,graph,"5"))

                
    
        
