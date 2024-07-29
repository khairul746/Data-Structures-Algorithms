class Graph:
    """
    Represents a graph data structure using an adjacency list.
    """

    def __init__(self):
        """
        Initializes an empty graph.
        """
        self.adj_list = {}

    def print_graph(self):
        """
        Prints the graph in a readable format.
        """
        vertices = sorted(self.adj_list.keys())  # Sort vertices for consistent output
        for vertex in vertices:
            print(f"{vertex}: {self.adj_list[vertex]}")

    def add_vertex(self, vertex):
        """
        Adds a new vertex to the graph.

        Args:
            vertex: The value of the vertex to add.

        Returns:
            True if the vertex was added successfully, False if it already exists.
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        """
        Adds an edge between two vertices in the graph.

        Args:
            v1: The first vertex.
            v2: The second vertex.

        Returns:
            True if the edge was added successfully, False if either vertex doesn't exist.
        """
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        """
        Removes an edge between two vertices in the graph.

        Args:
            v1: The first vertex.
            v2: The second vertex.

        Returns:
            True if the edge was removed successfully, False if either vertex or edge doesn't exist.
        """
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                return True
            except ValueError:
                pass  # Edge doesn't exist
        return False

    def remove_vertex(self, vertex):
        """
        Removes a vertex and all its edges from the graph.

        Args:
            vertex: The vertex to remove.

        Returns:
            True if the vertex was removed successfully, False if the vertex doesn't exist.
        """
        if vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                self.adj_list[neighbor].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
