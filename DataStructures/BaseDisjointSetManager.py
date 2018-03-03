from uuid import uuid4
from collections import defaultdict
from collections import deque
import random

class Node(object):    
    def __init__(self, instance):
        self.node = instance
        self.setptr = None
        self.next = None

class HeadNodeRefence(object):
    def __init__(self):
        self.start = None
        self.end = None
        self.set_id = None
        self.uuid = uuid4()
        self.rank = 0

class BaseDisjointSetManager(object):
    def __init__(self):        
        self.set_collection = deque()
        self._head_node_reference_mapping = {}
        self._node_mapping = defaultdict(set)

    
    def add_set_to_collection(self, set_instance=None):
        head_node_reference = HeadNodeRefence()

        if set_instance is None:
            set_instance = {}
        else:
            for item in set_instance:
                node = Node(item)
                node.setptr = head_node_reference
                if head_node_reference.start is None:
                    head_node_reference.start = node                    
                else:
                    curr_node.next = node
                
                curr_node = node
                head_node_reference.end = node
                head_node_reference.rank += 1

                # saving the mapping between element and node instance
                self._node_mapping[item].add(node)
            
        # adding id of this set to mapping head node reference instance
        head_node_reference.set_id = id(set_instance)
        self._head_node_reference_mapping[head_node_reference.set_id] = head_node_reference
        self.set_collection.append(head_node_reference)
        return set_instance
    
    def add_element_to_set_instance(self, element=None, set_instance=None):
        try:
            if set_instance is None:
                self.add_set_to_collection({element})
            else:
                head_node_reference = self._head_node_reference_mapping[id(set_instance)]
                node = Node(element)
                node.setptr = head_node_reference
                head_node_reference.end.next = node
                head_node_reference.end = node
                head_node_reference.rank += 1
                self._node_mapping[element].add(node)
            return element
        except:
            print("we GOT EXCEPTION !!!! :)")           
    
    def _find_by_node(self, node):
        raise Exception("_find_by_node must be implemented in derived class")

    
    def find(self, element=None):
        try:
            node = next(iter(self._node_mapping[element]))
            return self._find_by_node(node)
        except:
            raise Exception("No element passed to find")
    
    def _union_by_nodes(self, node1, node2):
        raise Exception("_union_by_nodes must be implemented in derived class")

    def union(self, element1, element2):
        if element1 is None or element2 is None:
            raise Exception("2 elements need to be passed for a union")
        
        try:
            node1 = next(iter(self._node_mapping[element1]))
            node2 = next(iter(self._node_mapping[element2]))

            return self._union_by_nodes(node1, node2)
        except:
            raise Exception('at least 1 of the elements do not exist in any set in the disjoint set collection')
    
    def _delete_by_node(self,node):
        raise Exception("_delete_by_node must be implemented in derived class")

    def delete(self, element, set_instance = None):
        node_set = self._node_mapping.get(element, None)
        if node_set is None:
            raise Exception('either element passed was None or element doesn\'t exist in any set in the disjoint set collection')
        else:
            node_to_be_deleted = None
            if set_instance is not None:
                try:
                    head_node_reference = self._head_node_reference_mapping[id(set_instance)]
                    for node in node_set:
                        if node.setptr == head_node_reference:
                            node_to_be_deleted = node
                            break
                except:
                    raise Exception('given set instance doesn\'t exist in the disjoint set collection')
            else:
                node_to_be_deleted = next(iter(node_set))

            if node_to_be_deleted is not None:
                self._delete_by_node(node_to_be_deleted)
                node_to_be_deleted.setptr.rank -= 1

    def __str__(self):
        buff = ''
        for set_ptr in self.set_collection:
            buff += '-------------------------------\n'
            buff += 'Set ' + str(set_ptr.uuid) +"\n"
            buff += '-------------------------------\n'
            buff += self._print(set_ptr.start)
        return buff
    
    def _print(self, start_node):
        raise Exception("_print must be implemented in derived class.")