# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
            # if insert value is greater than the default value
            if value > self.value:
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
        # then recursively call contains
        # is the target more than self.value and self.right
        # then recursively call contains

        # if not return false
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
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
