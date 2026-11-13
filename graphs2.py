from collections import deque
# 1. Represent the graph using an adjacency list
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

 
# 2. Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    print("BFS Traversal:")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print()


# 3. Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        print("DFS Traversal:")

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# 4. Main program
print("GRAPH TRAVERSAL PROGRAM")
print("1. Breadth-First Search (BFS)")
print("2. Depth-First Search (DFS)")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    bfs(graph, "A")

elif choice == "2":
    dfs(graph, "A")
    print()

else:
    print("Invalid choice. Please select 1 or 2.")