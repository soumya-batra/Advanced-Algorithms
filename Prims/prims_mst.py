from heapq import heapify, heappush, heappop
from node import TreeNode, GraphNode, Neighbor

class PrimsMST:
    def __init__(self):
        self.helper_heap = []
        self.mst_nodes_dict = {}

    def initialize_heap(self, nodes):
        self.helper_heap += [(node.edge_weight, node) for node in nodes]
        heapify(self.helper_heap)

    def put_in_heap(self, incident_node):
        # Check if incident node already exists in the heap
        heap_element = [(index, (weight, neighbor_node)) for index, (weight, neighbor_node) in enumerate(self.helper_heap) if neighbor_node.node.node_id == incident_node.node.node_id]

        # Node found in heap
        if len(heap_element) > 0:
            node_index_in_heap, (node_current_weight, _) = heap_element[0]

            # Update node in heap if a smaller edge weight is found than current
            if node_current_weight > incident_node.edge_weight:
                self.helper_heap[node_index_in_heap] = (incident_node.edge_weight, incident_node)
                heapify(self.helper_heap)


        # Node not found in heap - Add node to the heap as-is
        else:
            heappush(self.helper_heap, (incident_node.edge_weight, incident_node))

    def get_neighbors_not_in_mst(self, all_neighbors):
        return {neighbor for neighbor in all_neighbors if neighbor.node.node_id not in self.mst_nodes_dict}

    def run_prims(self, graph_root_node):

        # Add the initial root node to mst_nodes_dict
        root_tree_node = TreeNode(None, graph_root_node.node_id, 0)
        self.mst_nodes_dict[graph_root_node.node_id] = root_tree_node

        # Initialize helper heap with start node's neighbors
        self.initialize_heap(graph_root_node.get_neighbors())

        # Run Prim's
        while(len(self.helper_heap) > 0):

            # Retrieve minimum edge weight element
            _, min_weight_neighbor_node = heappop(self.helper_heap)

            # Add to mst
            curr_min_weight_treenode = TreeNode(parent_id = min_weight_neighbor_node.coneighbor_id, node_id = min_weight_neighbor_node.node.node_id, edge_weight = min_weight_neighbor_node.edge_weight)           
            self.mst_nodes_dict[min_weight_neighbor_node.coneighbor_id].add_child(curr_min_weight_treenode)
            self.mst_nodes_dict[min_weight_neighbor_node.node.node_id] = curr_min_weight_treenode

            # Add neighbors of minimum edge weight element to heap
            for neighbor in self.get_neighbors_not_in_mst(min_weight_neighbor_node.node.get_neighbors()):
                self.put_in_heap(neighbor)

        return root_tree_node

           

    


