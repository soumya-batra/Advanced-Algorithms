from uuid import uuid4

class BaseTreeNode:
    # data is of type object
    def __init__(self, edge_weight, child_nodes = None, data = None, parent_id = None, node_id = None):
        self.parent_id = parent_id
        self.node_id = uuid4() if node_id is None else node_id
        self.edge_weight = edge_weight    # edge weight between parent and child node
        self.children = [] if child_nodes is None else child_nodes
        self.data = data

    # get current node's id:
    def get_node_id(self):
        return self.get_node_id

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
        return 'parent id = {} ; node id = {}; weight = {}; data = {}'.format(self.parent_id, self.node_id, self.edge_weight, self.data)

class BaseTree:
    def __init__(self, root = None):
        self.root = root

    # If parent id/node is given, adds node as child to that parent. Else, inserts it randomly in the tree
    def insert_node(self, node, parent_id = None, parent_node = None):
        pass

    def delete_node(self, node):
        pass

    def search_node(self, node_id = None, node_data = None):
        if node_id is None and node_data is None:
            raise Exception('No data was passed to search')
        pass

    def traverse(self):
        pass