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
    def for_each(self, cb): # Recursive # Depth First Traversal
        cb(self.value) # callback with the value

        if self.left: # If theres values on the left
            self.left.for_each(cb) # return all the values on the left
        if self.right: # If theres values on the right
            self.right.for_each(cb) # Return all the values on the right

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None: # If there is a node on the left
            node.in_order_print(node.left) # print in order the nodes on the left

        print(node.value) # print node

        if node.right is not None: # If there is a node on the right
            node.in_order_print(node.right) # print in order the nodes on the right

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        node_queue = Queue() # create a node_queue
        node_queue.enqueue(node) # add current node to queue

        while node_queue.size > 0: # while queue is not empty
            node = node_queue.dequeue() # removes node from the front of the queue
            print(node.value) # print the value

            if node.left is not None: # If there is a node on the left
                node_queue.enqueue(node.left) # Add the node to the back of the queue

            if node.right is not None: # If there is a node on the right
                node_queue.enqueue(node.right) # Add the node to the back of the queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        node_stack = Stack() # create a node_stack
        node_stack.push(node) # push the current node onto stack

        while node_stack.size > 0: # while we have items on the stack
            node = node_stack.pop() # removes the node from the back of the stack
            print(node.value) # print the current value

            if node.left is not None: # If there is a left node
                node_stack.push(node.left) # adds the node to the back of the stack

            if node.right is not None: # If there is a right node
                node_stack.push(node.right) # Adds the node to the back of the stack

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value) # print the current value
        if node.left: # If there's a node left
            self.pre_order_dft(node.left) # visits the first node on the left
        if node.right: # If there's a node right
            self.pre_order_dft(node.right) # visits the first node on the right

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left: # if there's a node left
            self.post_order_dft(node.left) # visits each child before the main node
        if node.right: # if there's a node right
            self.post_order_dft(node.right) # visits each child before the main node
        print(node.value) # print current value
