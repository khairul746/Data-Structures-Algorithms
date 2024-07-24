class Node:
    """
    Represents a node in a doubly linked list.
    """
    def __init__(self, value):
        """
        Initializes a new node with the given value.

        Args:
            value: The data to store in the node.
        """
        self.value = value
        self.next = None  # Pointer to the next node in the list.
        self.prev = None  # Pointer to the previous node in the list.

class DoublyLinkedList:
    """
    Implements a doubly linked list data structure.
    """
    def __init__(self, value):
        """
        Initializes a new doubly linked list with a single node.

        Args:
            value: The initial value for the first node.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Prints the values of all nodes in the list.
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Adds a new node with the given value to the end of the list.

        Args:
            value: The value to store in the new node.

        Returns:
            True if the operation was successful, False otherwise.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        Removes and returns the last node from the list.

        Returns:
            The removed node or None if the list is empty.
        """
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        """
        Adds a new node with the given value to the beginning of the list.

        Args:
            value: The value to store in the new node.

        Returns:
            True if the operation was successful, False otherwise.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """
        Removes and returns the first node from the list.

        Returns:
            The removed node or None if the list is empty.
        """
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        """
        Retrieves the node at the specified index in the doubly linked list.

        Args:
            index: The index of the node to get (0-based indexing).

        Returns:
            The node at the specified index or None if the index is out of bounds.
        """

        if index < 0 or index >= self.length:
            return None

        temp = self.head
        if index < self.length / 2:
            # Traverse from the beginning for faster access for lower indices
            for _ in range(index):
                temp = temp.next
        else:
            # Traverse from the end for faster access for higher indices
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp

    def set_value(self, index, value):
        """
        Updates the value of the node at the specified index in the doubly linked list.

        Args:
            index: The index of the node to modify (0-based indexing).
            value: The new value to store in the node.

        Returns:
            True if the operation was successful, False otherwise (e.g., index out of bounds).
        """

        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """
        Inserts a new node with the given value at the specified index in the doubly linked list.

        Args:
            index: The index to insert the new node at (0-based indexing).
            value: The value to store in the new node.

        Returns:
            True if the operation was successful, False otherwise (e.g., index out of bounds).
        """

        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)  # Use prepend for insertion at the beginning
        if index == self.length:
            return self.append(value)  # Use append for insertion at the end

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        """
        Removes the node at the specified index from the doubly linked list.

        Args:
            index: The index of the node to remove (0-based indexing).

        Returns:
            The removed node or None if the index is out of bounds.
        """

        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()  # Use pop_first for removal at the beginning
        if index == self.length - 1:
            return self.pop()  # Use pop for removal at the end

        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp
