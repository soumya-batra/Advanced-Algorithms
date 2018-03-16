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

    def dfs_traverse(self, node_fobject_list = [print], edge_fobject_list=[print]):
        self._dfs_recursive_traverse(self.start_node, node_fobject_list = node_fobject_list, edge_fobject_list=edge_fobject_list)
    
    def _dfs_recursive_traverse(self, node, visited_nodes=set(), node_fobject_list = None, edge_fobject_list=None):
        if not (node is None or node in visited_nodes):
            [fobject(node) for fobject in node_fobject_list if fobject is not None]
            for edge in node.edges:
                [fobject(node, edge) for fobject in edge_fobject_list if fobject is not None]
                visited_nodes.add(node)
                self._dfs_recursive_traverse(edge.coneighbor_node, node_fobject_list = node_fobject_list, edge_fobject_list = edge_fobject_list)
    
    def _collect_nodes(self, node):
        if hasattr(self, "unique_nodes"):
            self.unique_nodes.add(node)
        else:
            self.unique_nodes = set()

    def _collect_edges(self, node, edge):
        if hasattr(self, "unique_edges"):
            self.unique_edges.add(edge)  
        else:
            self.unique_edges = set()

    def get_nodes_and_edges(self):
        self.dfs_traverse(node_fobject_list = [self._collect_nodes], edge_fobject_list=[self._collect_edges])
        return self.unique_nodes, self.unique_edges
