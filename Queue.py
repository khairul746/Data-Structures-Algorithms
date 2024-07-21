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

class Queue:
    """
    Implements a queue data structure using a linked list.
    """
    def __init__(self, value):
        """
        Initializes a new queue with a single node.

        Args:
            value: The initial value for the first element of the queue.
        """
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        """
        Prints the values of all elements in the queue, starting from the front.
        """
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        """
        Adds a new element (value) to the back of the queue (FIFO - First In, First Out).

        Args:
            value: The value to add to the queue.

        Returns:
            True if the operation was successful, False otherwise (e.g., memory allocation error).
        """
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue (FIFO - First In, First Out).

        Returns:
            The removed element or None if the queue is empty.
        """
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
