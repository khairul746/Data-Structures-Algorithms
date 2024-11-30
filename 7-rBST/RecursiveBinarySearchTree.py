class Node:
    """
    A class representing a node in a binary search tree.

    Attributes:
        value: The value stored in the node.
        left: A reference to the left child node.
        right: A reference to the right child node.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    A class representing a binary search tree.

    Methods:
        insert(value): Public method to insert a value into the tree.
    """
    def __init__(self):
        self.root = None
    def __r_insert(self, current_node, value):
        """
        Recursively inserts a value into the binary search tree.

        Args:
            current_node (Node): The current node being checked.
            value: The value to insert into the tree.

        Returns:
            Node: The updated node after insertion.
        """
        # If the current node is None, create a new node with the value
        if current_node is None:
            return Node(value)
        
        # If the value is less than the current node's value, insert into the left subtree
        if value < current_node.value:
            current_node.left = self.__recursive_insert(current_node.left, value)
        
        # If the value is greater than the current node's value, insert into the right subtree
        elif value > current_node.value:
            current_node.right = self.__recursive_insert(current_node.right, value)
        
        # Return the current node
        return current_node

    def r_insert(self, value):
        """
        Inserts a value into the binary search tree.

        Args:
            value: The value to insert into the tree.
        """
        # If the tree is empty, create a new root node
        if self.root is None:
            self.root = Node(value)
        else:
            # Insert the value recursively starting from the root
            self.__r_insert(self.root, value)

