from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

def bfs(start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        current_node = queue.popleft()
        print(current_node.value, end=" ")

        for neighbor in current_node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node0.neighbors = [node1, node2]
node1.neighbors = [node2]
node2.neighbors = [node3]
node3.neighbors = [node1, node2]

print("Breadth First Traversal:")
bfs(node0)