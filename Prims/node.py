class TreeNode:
    def __init__(self, parent_id, node_id, edge_weight, child_nodes = []):
        self.parent_id = parent_id
        self.node_id = node_id
        self.edge_weight = edge_weight    # edge weight between parent and child node
        self.children = [] #child_nodes

    # child_node of type TreeNode
    def add_child(self, child_node):
        self.children.append(child_node)

    def get_children(self):
        return self.children
    
    def to_string(self):
        string_rep = self.to_string_without_children() + '\n'
        sep = '\t -- '
        for child in self.children:
            string_rep += sep + child.__to_string_without_children() + '\n'
        return string_rep

    def to_string_without_children(self):
        return 'parent id = {} ; node id = {}; weight = {}'.format(self.parent_id, self.node_id, self.edge_weight)


class GraphNode:
    # An element of neighbors is of type Neighbor
    def __init__(self, node_id, neighbors = []):
        self.node_id = node_id
        self.neighbors = []#neighbors

    def add_neighbor(self, neighbor_node, edge_weight):
        self.neighbors.append(Neighbor(neighbor_node, self.node_id, edge_weight))

    def get_neighbors(self):
        return self.neighbors
    
class Neighbor:
    # node is of type GraphNode having this instance of neighbor
    def __init__(self, node, coneighbor_id, edge_weight):
        self.node = node
        self.coneighbor_id = coneighbor_id
        self.edge_weight = edge_weight