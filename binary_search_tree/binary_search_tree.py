import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value: # If the value is less than the base value
            if not self.left: # If there's no left value
                self.left = BinarySearchTree(value) # Make given value the top left value
            else: # if it is left
                self.left.insert(value) # insert the new value
        else: # if the value is more than the base value
            if not self.right: # if there's no right value
                self.right = BinarySearchTree(value) # make given value the top right value
            else: # if it is right
                self.right.insert(value) # insert the new value


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target: # If the top value == target
            return True # Return true

        if target < self.value: # If the target value is less than the top node
            if not self.left: # If there is no left values
                return False # Return false
            else: # If there is left values
                return self.left.contains(target) # Search the left for the target value
        else: # If the target value is more than the top node
            if not self.right: # If there's no right values
                return False # Return false
            else: # If there's right values
                return self.right.contains(target) # Search for the target value

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right: # if there's no right value
            return self.value # make the top value the max
        else: # if there's right values
            return self.right.get_max() # find the max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value) # callback with the value

        if self.left: # If theres values on the left
            self.left.for_each(cb) # return all the values on the left
        if self.right: # If theres values on the right
            self.right.for_each(cb) # Return all the values on the right

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
