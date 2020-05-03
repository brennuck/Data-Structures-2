import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value): # adds new items to the end of an array, and returns the new length
        self.storage.add_to_tail(value) # Add new item to the back of the queue
        self.size += 1 # Add 1 for the new item

    def pop(self): # removes the last element of an array, and returns that element.
        if self.size > 0: # If the size of the queue is greater than 0
            self.size -= 1 # Remove 1 from the size
            return self.storage.remove_from_tail() # Remove the last item from the queue
        else: # If the size of the queue is 0
            return None # Return none

    def len(self):
        return len(self.storage)
