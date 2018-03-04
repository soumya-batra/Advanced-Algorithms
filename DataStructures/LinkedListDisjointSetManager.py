from BaseDisjointSetManager import *

class LinkedListDisjointSetManager(BaseDisjointSetManager):
    def add_set_to_collection(self, set_instance = None):
        return self._add_set_to_collection(set_instance, set_setptr_to_prev = False)

    def add_element_to_set_instance(self, element = None, set_instance = None):
        return self._add_element_to_set_instance(element, set_instance, set_setptr_to_prev = False)

    def _find_by_node(self, node):
        if node is None:
            raise Exception('empty node passed')
        return node.setptr.uuid
    
    def _union_by_nodes(self, node1, node2):
        if node1 is None or node2 is None:
            raise Exception('cannot take union of empty nodes')
        
        #setptr_1 contains the pointer to set with lowest number of elements
        setptr_1 = node1.setptr
        setptr_2 = node2.setptr
        if setptr_1.rank > setptr_2.rank:
            setptr_1, setptr_2 = setptr_2, setptr_1
        
        #make elements of smaller set point to the set pointer of bigger set
        curr_node = setptr_1.start
        while curr_node is not None:
            curr_node.setptr = setptr_2
            curr_node = curr_node.next
        
        #point end of bigger set to start of smaller set
        setptr_2.end.next = setptr_1.start
        setptr_2.end = setptr_1.end

        #remove smaller set from the collection
        self.set_collection.remove(setptr_1)
        del self._head_node_reference_mapping[setptr_1.set_id]

    def _delete_by_node(self, node, delete_set_if_empty = False):
        if node is None:
            raise Exception("empty node is passed")
        node_setptr = node.setptr
        curr_node = node_setptr.start
        # if node is the first element
        if node_setptr.start == node:
            node_setptr.start = curr_node.next
            # single element collection
            if node_setptr.end == node:
                node_setptr.end = None
                if delete_set_if_empty:
                    # remove the head node reference if only single element
                    self.set_collection.remove(node_setptr)
        else:
            # node lies in betwen 1st and last element
            while curr_node.next != node:
                curr_node = curr_node.next
            curr_node.next = node.next
            # node is the last element
            if node_setptr.end == node:            
                node_setptr.end = curr_node

        # rank update
        node.setptr.rank -= 1

        # discard from mapping only if it exists
        self._node_mapping[node.node].discard(node)
        del node

        