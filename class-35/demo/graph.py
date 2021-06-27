from collections import deque


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)


class Stack:
    pass


class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """Adds value to a node and adds the node to a graph"""
        # new node
        v = Vertex(value)
        # add to the adjacency_list
        self._adjacency_list[v] = []
        return v

    def size(self):
        return len(self._adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Adds an edge to the graph"""
        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not found in graph")

        self._adjacency_list[start_vertex].append(Edge(end_vertex, weight))

    def get_nodes(self):
        """Get all of the nodes in the graph"""
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        """Get all of the neighbors of a vertex"""
        return self._adjacency_list.get(vertex, [])

    def breadth_first_search(self, start_vertex, action=(lambda x: None)):
        queue = Queue()
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            action(current_vertex)
            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor_vertex = edge.vertex

                if neighbor_vertex in visited:
                    continue
                else:
                    visited.add(neighbor_vertex)
                queue.enqueue(neighbor_vertex)
    
if __name__ == "__main__":
    g = Graph()
    node1 = g.add_node('node1')
    node2 = g.add_node('node2')
    g.add_edge(node1, node2)

    g.breadth_first_search(node1, lambda v: print(v.value))