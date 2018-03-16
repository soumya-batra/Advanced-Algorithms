from algorithms.mst.base_mst import *
from data_structures.disjoint_set.TreeBasedDisjointSetManager import TreeBasedDisjointSetManager
from operator import attrgetter

class KruskalsMST(BaseMST):
    def __init__(self):
        self.mst_vertices_disjoint_set = TreeBasedDisjointSetManager()
        self.tree_node_dict = {}
        self.mst_root_node = None
    
    def run(self, graph):
        if graph is None:
            raise Exception("No input graph passed")

        nodes, edges = graph.get_nodes_and_edges()

        for node in nodes:
            self.mst_vertices_disjoint_set.add_set_to_collection({node})
            self.tree_node_dict[node.node_id] = BaseTreeNode(edge_weight=None, data=node.data, node_id=node.node_id)

            if self.mst_root_node is None:
                self.mst_root_node = node
        
        edges = sorted(edges, key = attrgetter("edge_weight"))

        # pick the edge based on weight - in ascending order of weights
        for edge in edges:
            src_vertex = edge.node
            dest_vertex = edge.coneighbor_node

            if self.mst_vertices_disjoint_set.find(src_vertex) != self.mst_vertices_disjoint_set.find(dest_vertex):
                self.mst_vertices_disjoint_set.union(src_vertex, dest_vertex)
                self._add_edge_to_mst(src_vertex, edge)


    def _add_edge_to_mst(self, src_vertex, edge):
        child_node = self.tree_node_dict[edge.coneighbor_node.node_id]
        child_node.edge_weight = edge.edge_weight
        self.tree_node_dict[src_vertex.node_id].add_child(child_node)



    


        
        



        

