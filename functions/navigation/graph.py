from functions.navigation.edge import Edge


class Graph:
    def __init__(self):
        self.node_list = []

    def add_node(self, node):
        self.node_list.append(node)

    def add_edge(self, start, end, dist):
        forward_edge = Edge(start, end, dist)
        reverse_edge = Edge(end, start, dist)

        # adding edges to appropriate nodes
        start.edges.append(forward_edge)
        end.edges.append(reverse_edge)
