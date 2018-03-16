import sys, os
from pathlib import Path
sys.path.insert(0,  str(Path(os.path.abspath('__file__')).parents[2] ))
from collections import deque
from LinkedListDisjointSetManager import LinkedListDisjointSetManager
from TreeBasedDisjointSetManager import TreeBasedDisjointSetManager

def run(sysargs):
    
    # Create some data
    s1 = {1,2,3,4}  
    #lmgr = LinkedListDisjointSetManager()
    lmgr = TreeBasedDisjointSetManager()
    lmgr.add_set_to_collection(s1)
    print("lmgr.add_set_to_collection(s1)", lmgr)  
    # s1 = {1,2,3,4}

    s2 = lmgr.add_set_to_collection({4,5,6})
    print("lmgr.add_set_to_collection({4,5,6})", lmgr)
    # s2 = {4,5,6}

    lmgr.add_element_to_set_instance(8)
    print("lmgr.add_element_to_set_instance(8)", lmgr)
    # s3 = {8}

    lmgr.add_element_to_set_instance(9, s2)
    print("lmgr.add_element_to_set_instance(9, s2)", lmgr)
    # s2 = {4,5,6,9}

    # see the uuid of head reference of each set
    print("lmgr.find(4)", lmgr.find(4))
    # uuid of one of these: s1/s2

    print("lmgr.find(2)", lmgr.find(2))
    # uuid of s1

    #print("lmgr.find(22)", lmgr.find(22))
    # exception


    lmgr.union(4, 8)
    print("lmgr.union(4, 8)", lmgr)
    # final sets is one of the two:
    # s1 = {1,2,3,4,8} ; s2 = {4,5,6,9}
    # or s1 = {1,2,3,4} ; s2 = {4,5,6,8,9}

    #lmgr.union(4,22)
    #print("lmgr.union(4,22)", lmgr)
    # should not work :D -> Exception

    lmgr.delete(6)
    print("lmgr.delete(6)", lmgr)
    # s2 = {4,5,9}
    
    lmgr.delete(4, s2)
    print("lmgr.delete(4)", lmgr)
    # either s1 = {1,2,3} or s2 = {5,6,8,9}

    # lmgr.delete(22)
    # print("lmgr.delete(22)", lmgr)
    # exception

if __name__ == '__main__':
    run(sys.argv[1:])