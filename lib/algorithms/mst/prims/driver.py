import sys, os
from pathlib import Path
sys.path.insert(0,  str(Path(os.path.abspath('__file__')).parents[3] ))
from data_structures.tree.base_tree import *
from data_structures.graph.base_graph import BaseGraphNode, Graph, Edge
from algorithms.mst.prims.prims_mst import PrimsMST
from collections import deque

def run(sysargs):
    
    # Create some data
    graph_nodes = [BaseGraphNode(data = i) for i in range(8)]

    graph_nodes[0].add_edge(graph_nodes[1], 2.5)

    graph_nodes[1].add_edge(graph_nodes[0], 2.5)
    graph_nodes[1].add_edge(graph_nodes[2], 3)
    graph_nodes[1].add_edge(graph_nodes[4], 2)

    graph_nodes[2].add_edge(graph_nodes[1], 3)
    graph_nodes[2].add_edge(graph_nodes[3], 5.5)

    graph_nodes[3].add_edge(graph_nodes[2], 5.5)
    graph_nodes[3].add_edge(graph_nodes[4], 7)
    graph_nodes[3].add_edge(graph_nodes[6], 4)

    graph_nodes[4].add_edge(graph_nodes[1], 2)
    graph_nodes[4].add_edge(graph_nodes[3], 7)
    graph_nodes[4].add_edge(graph_nodes[5], 8)
    graph_nodes[4].add_edge(graph_nodes[6], 6)

    graph_nodes[5].add_edge(graph_nodes[4], 8)

    graph_nodes[6].add_edge(graph_nodes[3], 4)
    graph_nodes[6].add_edge(graph_nodes[4], 6)

    traverse_tree(PrimsMST().run(graph_nodes[5]))
    traverse_tree(PrimsMST().run(graph_nodes[0]))
    traverse_tree(PrimsMST().run(graph_nodes[3]))


def traverse_tree(tree_node):
    helper_queue = deque()
    helper_queue.append(tree_node)
    while len(helper_queue) > 0:
        curr_node = helper_queue.popleft()
        print(curr_node.to_string_without_children() + '----------------------------')
        for child in curr_node.get_children():
            helper_queue.append(child)


if __name__ == '__main__':
    run(sys.argv[1:])