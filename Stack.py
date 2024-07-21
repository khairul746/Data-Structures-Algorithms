class Node:
    """
    Represents a node in a linked list.
    """
    def __init__(self, value):
        """
        Initializes a new node with the given value.

        Args:
            value: The data to store in the node.
        """
        self.value = value
        self.next = None  # Pointer to the next node in the list.

class Stack:
    """
    Implements a stack data structure using a linked list.
    """
    def __init__(self, value):
        """
        Initializes a new stack with a single node.

        Args:
            value: The initial value for the top element of the stack.
        """
        new_node = Node(value)
        self.top = new_node
        self.height = 1  # Keeps track of the number of elements in the stack

    def print_stack(self):
        """
        Prints the values of all elements in the stack, starting from the top.
        """
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        """
        Pushes a new element (value) onto the top of the stack.

        Args:
            value: The value to add to the stack.

        Returns:
            True if the operation was successful, False otherwise (e.g., memory allocation error).
        """
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        """
        Removes and returns the element at the top of the stack (LIFO - Last In, First Out).

        Returns:
            The removed element or None if the stack is empty.
        """
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
