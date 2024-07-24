class Node:
    """Represents a node in a binary search tree."""

    def __init__(self, value):
        """
        Initializes a new node with the given value.

        Args:
            value: The value to store in the node.
        """
        self.value = value
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child

class BinarySearchTree:
    """Represents a binary search tree."""

    def __init__(self):
        """Initializes an empty binary search tree."""
        self.root = None

    def insert(self, value):
        """
        Inserts a new value into the binary search tree.

        Args:
            value: The value to insert.

        Returns:
            True if the insertion was successful, False if the value already exists.
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False  # Duplicate value
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        """
        Checks if a given value exists in the binary search tree.

        Args:
            value: The value to search for.

        Returns:
            True if the value exists, False otherwise.
        """
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
