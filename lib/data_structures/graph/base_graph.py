from uuid import uuid4

class BaseGraphNode:
    # An element of edges is of type Edge
    def __init__(self, edges = None, data = None):
        self.node_id = uuid4()
        self.edges = [] if edges is None else edges #edges contains neighbors information
        self.data = data

    def get_node_id(self):
        return self.node_id

    # if directed edges are used - make sure to add edge from source to dest only
    def add_edge(self, neighbor_node, edge_weight, is_bidirectional = False):
        edge = Edge(self, neighbor_node, edge_weight)
        self.edges.append(edge)

        if is_bidirectional:
            neighbor_node.add_edge(self, edge_weight, is_bidirectional=False)

    def get_edges(self):
        return self.edges

class UndirectedGraphNode(BaseGraphNode):
    # all edges are undirected
    def add_edge(self, neighbor_node, edge_weight):
        super.add_edge(neighbor_node, edge_weight, True)

class DirectedGraphNode(BaseGraphNode):
    # all edges are directed
    def add_edge(self, neighbor_node, edge_weight):
        super.add_edge(neighbor_node, edge_weight, False)

class Edge:
    # node is of type GraphNode having this instance of edge
    def __init__(self, node, coneighbor_node, edge_weight):
        self.node = node
        self.coneighbor_node = coneighbor_node
        self.edge_weight = edge_weight

class Graph:
    def __init__(self, start_node = None):
        self.start_node = start_node

    def delete_node(self, node_id = None, node_data = None, node = None):
        pass

    def search_node(self, node_id = None, node_data = None):
        pass

    def traverse(self):
        pass
