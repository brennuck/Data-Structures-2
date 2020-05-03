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
        # check if empty
        # if empty put node here / at root
        # else
        # if new < node.value
        # leftnode.insert value
        # if >=
        # rightnode.insert value
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # find:
        # if node is none
            # return false
        # if node.value == findvalue
            # return true
        # else
            # if find < node.value
                # find on left node
            # else
                # find on right node
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # if theres a node to the right
        # get max on right
        # else
        # return node.value
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

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
