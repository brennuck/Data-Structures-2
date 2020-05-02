from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.order = DoublyLinkedList() # Store the order
        self.storage = dict() # Store key value pairs
        self.size = 0 # Current size
        self.limit = limit # Limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage: # Checks if the key that is associated with the value is in storage
            node = self.storage[key] # Pull the value of dict using the key
            self.order.move_to_end(node) # Move the value to the end
            return node.value[1] # update the position in the list
        else: # If there isn't a key-value pair
            return None # Return none

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
        if key in self.storage: # if key is in storage
            node = self.storage[key] # pull the value of dict using the key
            node.value = (key, value) # assign values
            self.order.move_to_end(node) # Move the value to the end
            return # return
        if self.size == self.limit: # if the storage is full
            del self.storage[self.order.head.value[0]] # Delete the oldest entry
            self.order.remove_from_head() # Remove the value from the list
            self.size -= 1 #  - 1 from the storage
        self.order.add_to_tail((key, value)) # Add the new pair to the dict
        self.storage[key] = self.order.tail # The value assigned to the last item on the list (most recently added)
        self.size += 1 # Adding a value to the size
