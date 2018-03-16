from heapq import heapify, heappush, heappop
from algorithms.mst.base_mst import *

class PrimsMST(BaseMST):
    def __init__(self):
        self.helper_heap = []
        self.mst_nodes_dict = {}

    def initialize_heap(self, edges):
        self.helper_heap += [(edge.edge_weight, edge) for edge in edges]
        heapify(self.helper_heap)

    def put_in_heap(self, incident_edge):
        # Check if incident node already exists in the heap
        heap_element = [(index, (weight, edge)) for index, (weight, edge) in enumerate(self.helper_heap) if edge.coneighbor_node.node_id == incident_edge.coneighbor_node.node_id]

        # Node found in heap
        if len(heap_element) > 0:
            node_index_in_heap, (node_current_weight, _) = heap_element[0]

            # Update node in heap if a smaller edge weight is found than current
            if node_current_weight > incident_edge.edge_weight:
                self.helper_heap[node_index_in_heap] = (incident_edge.edge_weight, incident_edge)
                heapify(self.helper_heap)


        # Node not found in heap - Add node to the heap as-is
        else:
            heappush(self.helper_heap, (incident_edge.edge_weight, incident_edge))

    def get_neighbors_not_in_mst(self, all_neighbors):
        return {neighbor for neighbor in all_neighbors if neighbor.coneighbor_node.node_id not in self.mst_nodes_dict}

    def run(self, graph_root_node):

        # Add the initial root node to mst_nodes_dict
        root_tree_node = BaseTreeNode(edge_weight = 0, data = graph_root_node.data, node_id=graph_root_node.node_id)
        self.mst_nodes_dict[graph_root_node.node_id] = root_tree_node

        # Initialize helper heap with start node's neighbors
        self.initialize_heap(graph_root_node.get_edges())

        # Run Prim's
        while(len(self.helper_heap) > 0):

            # Retrieve minimum edge weight element
            _, min_weight_edge = heappop(self.helper_heap)

            # Add to mst
            curr_min_weight_treenode = BaseTreeNode(edge_weight = min_weight_edge.edge_weight, data = min_weight_edge.coneighbor_node.data, parent_id = min_weight_edge.node.node_id, node_id = min_weight_edge.coneighbor_node.node_id)           
            self.mst_nodes_dict[min_weight_edge.node.node_id].add_child(curr_min_weight_treenode)
            self.mst_nodes_dict[min_weight_edge.coneighbor_node.node_id] = curr_min_weight_treenode

            # Add neighbors of minimum edge weight element to heap
            for edge in self.get_neighbors_not_in_mst(min_weight_edge.coneighbor_node.get_edges()):
                self.put_in_heap(edge)

        return root_tree_node

           

    


