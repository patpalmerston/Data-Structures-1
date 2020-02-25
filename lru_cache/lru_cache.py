from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list.py')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.curr_node_number = 0
        self.dll_order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # look to see if key is in storage first
        if key in self.storage:
            # grab the value of the  node
            node = self.storage[key]
            # move to the end or most used spot
            self.dll_order.move_to_end(node)
            # return the value of the node which is the second index of the pair
            return node.value[1]
        # if node does not exist return None
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # STEP 1
        # add new key value pair to the cache as the newest item
        self.dll_order.add_to_tail((key, value))
        # add new tail to storage
        self.storage[key] = self.dll_order.tail
        # increment the curr nod number
        self.curr_node_number += 1
