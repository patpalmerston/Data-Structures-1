from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        return f"{self.value}"

    # Insert the given value into the tree
    def insert(self, value):
        # check to see if there is a value
        if self.value:
            # if there is a value
            # if insert value is less than the default value
            if value < self.value:
                # if there is no left value make new BST node
                if self.left is None:
                    self.left = BinarySearchTree(value)
                # else recursively call insert on the left side
                else:
                    self.left.insert(value)
            # if insert value is greater than the default value/ use the = to push duplicates into oneside or the other depending on the tests
            if value >= self.value:
                # if there is no right value make new BST node
                if self.right is None:
                    self.right = BinarySearchTree(value)
                # else recursively call insert on the right side
                else:
                    self.right.insert(value)

        # else there is no value than this value becomes the self.value(default value)
        else:
            self.value = value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if target is equal to default value(self.value)
        if target == self.value:
            # return True
            return True
        # is the target less than self.value and self.left
        elif target < self.value and self.left:
            # then recursively call contains
            return self.left.contains(target)
        # is the target more than self.value and self.right/ also = searches for duplicates
        elif target >= self.value and self.right:
            # then recursively call contains
            return self.right.contains(target)
        # if not return false
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if there is a right then call get_max until we return the last node to the right
        if self.right:
            return self.right.get_max()
        # else return self.value
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # call back is a function that appends x to an array
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # use call back on the root
        cb(self.value)
        # if there is a left call for_each(cb) on each node value
        if self.right:
            self.right.for_each(cb)
        # if there is a left call for_each(cb) on each node value
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # if the node passed in has value
        if self.value:
            # recurse down left child
            if self.left:
                self.left.in_order_print(self.left)
                print(self.value)
            # recurse down right child
            if self.right:
                self.right.in_order_print(self.right)
                # print(self.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
# breadth first is like a que

    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
# depth first is like a stack

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
