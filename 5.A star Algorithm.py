import heapq

class Graph:
    def _init_(self):
        self.graph = {}
        self.heuristics = {}

    def add_edge(self, node, neighbor, cost):
        if node not in self.graph:
            self.graph[node] = {}
        self.graph[node][neighbor] = cost

    def add_heuristic(self, node, heuristic_value):
        self.heuristics[node] = heuristic_value

    def get_neighbors(self, node):
        return self.graph.get(node, {})

def astar(graph, start, goal):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (0, start, None))
    while open_list:
        f_cost, current_node, parent = heapq.heappop(open_list)
        if current_node == goal:
            path = []
            while parent:
                path.append(current_node)
                current_node, parent = parent, graph.get_neighbors(parent).get(current_node)
            path.append(start)
            path.reverse()
            return path, f_cost
        closed_set.add(current_node)
        for neighbor, cost in graph.get_neighbors(current_node).items():
            if neighbor not in closed_set:
                g_cost = f_cost + cost
                h_cost = graph.heuristics.get(neighbor, 0)  # Get heuristic value or default to 0
                f_cost = g_cost + h_cost
                heapq.heappush(open_list, (f_cost, neighbor, current_node))
    return None, None

# Create a graph object
graph = Graph()

# User input for graph edges and heuristic values
while True:
    edge_input = input("Enter an edge (node neighbor cost), or type 'done' to finish: ")
    if edge_input.lower() == 'done':
        break
    parts = edge_input.split()
    if len(parts) == 3:
        node, neighbor, cost = parts
        if node.isalpha() and neighbor.isalpha():
            try:
                cost = int(cost)
                graph.add_edge(node, neighbor, cost)
            except ValueError:
                print("Invalid input. Please enter a valid numeric value for the cost.")
        else:
            print("Invalid input. Node and neighbor must be alphabetical characters.")
    else:
        print("Invalid input. Please enter an edge in the format 'node neighbor cost'.")

# User input for heuristic values
for node in graph.graph.keys():
    heuristic_value_input = input(f"Enter heuristic value for node {node}: ")
    if heuristic_value_input.replace(".", "").isdigit():
        heuristic_value = float(heuristic_value_input)
        graph.add_heuristic(node, heuristic_value)
    else:
        print("Invalid input. Please enter a valid numeric value for the heuristic.")

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path, estimated_cost = astar(graph, start, goal)

if path:
    print("Path found:", path)
    print("Estimated cost:", estimated_cost)
else:
    print("No path found.")
#Enter an edge (node neighbor cost), or type 'done' to finish: A B 2
#Enter an edge (node neighbor cost), or type 'done' to finish: A C 4
#Enter an edge (node neighbor cost), or type 'done' to finish: B D 5
#Enter an edge (node neighbor cost), or type 'done' to finish: C D 3
#Enter an edge (node neighbor cost), or type 'done' to finish: D E 2
#Enter an edge (node neighbor cost), or type 'done' to finish: DONE
#Enter heuristic value for node A: 5
#Enter heuristic value for node B: 3
#Enter heuristic value for node C: 4
#Enter heuristic value for node D: 2
#Enter start node: A
#Enter goal node: E
