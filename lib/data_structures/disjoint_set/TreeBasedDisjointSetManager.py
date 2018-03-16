from data_structures.disjoint_set.BaseDisjointSetManager import *

class TreeBasedDisjointSetManager(BaseDisjointSetManager):
    def add_set_to_collection(self, set_instance = None):
        return self._add_set_to_collection(set_instance, set_setptr_to_prev = True)

    def add_element_to_set_instance(self, element = None, set_instance = None):
        return self._add_element_to_set_instance(element, set_instance, set_setptr_to_prev = True)

    def _find_by_node(self, node):
        parent_node = self.__find_by_path_compression(node)
        return parent_node.setptr.uuid
    
    def __find_by_path_compression(self, node):
        if node is None:
            raise Exception('NoneType node is passed')
        # base condition - return parent node
        if getattr(node.setptr, 'start', None) == node:
            #print('parent:' , node.node)
            return node
        else:
            node.setptr = self.__find_by_path_compression(node.setptr)
            #print(node.setptr.node)
            return node.setptr
    
    def _union_by_nodes(self, node1, node2):
        parent_node1 = self.__find_by_path_compression(node1)
        parent_node2 = self.__find_by_path_compression(node2)

        # setptr_1 and parent_node1 correspond to smaller rank tree
        setptr1 = parent_node1.setptr
        setptr2 = parent_node2.setptr

        if setptr1.rank > setptr2.rank:
            setptr1, setptr2 = setptr2, setptr1
            parent_node1, parent_node2 = parent_node2, parent_node1

        # merge set1 to set 2
        setptr2.end.next = parent_node1
        setptr2.end = parent_node1.setptr.end
        parent_node1.setptr = parent_node2

        # rank update
        setptr2.rank += setptr1.rank

        # delete from memory
        del self._head_node_reference_mapping[setptr1.set_id]

    def _delete_by_node(self, node, delete_set_if_empty = False):
        parent_node = self.__find_by_path_compression(node)
        setptr = parent_node.setptr
        if node == parent_node:
            if node == setptr.end:      # single element
                setptr.end = setptr.start = None
                if delete_set_if_empty:
                    self.set_collection.remove(setptr)
            else:
                # swap values of parent node and end node
                parent_node.node, setptr.end.node = setptr.end.node, parent_node.node
                node = setptr.end

        curr_node = parent_node
        while(curr_node.next != node):
            curr_node = curr_node.next
        curr_node.next = node.next
        if node == setptr.end:
            setptr.end = curr_node
        setptr.rank -= 1
        self._node_mapping[node.node].discard(node) 
        del node

        