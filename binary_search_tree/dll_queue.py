import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value) # Add new item to the back of the queue
        self.size += 1 # plus 1 on the size

    def dequeue(self):
        if self.size > 0: # If size is greater than 0
            self.size -= 1 # Remove 1
            return self.storage.remove_from_head() # Remove the item from the front
        else: # If size is 0
            return None # Then just return none

    def len(self):
        return len(self.storage)
