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

class LinkedList:
    """
    Implements a linked list data structure.
    """
    def __init__(self, value):
        """
        Initializes a new linked list with a single node.

        Args:
            value: The initial value for the first element of the list.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Prints the values of all elements in the list, starting from the head.
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Adds a new element (value) to the end of the linked list.

        Args:
            value: The value to add to the list.

        Returns:
            True if the operation was successful, False otherwise (e.g., memory allocation error).
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        Removes and returns the last element from the linked list (FIFO - First In, First Out).

        Returns:
            The removed element or None if the list is empty.
        """
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
        return temp

    def prepend(self, value):
        """
        Adds a new element (value) to the beginning of the linked list.

        Args:
            value: The value to add to the list.

        Returns:
            True if the operation was successful, False otherwise (e.g., memory allocation error).
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """
        Removes and returns the first element from the linked list (FIFO - First In, First Out).

        Returns:
            The removed element or None if the list is empty.
        """
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        """
        Retrieves the element at a specific index in the linked list.

        Args:
            index: The zero-based index of the element to get.

        Returns:
            The element at the specified index or None if the index is out of range.
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        """
        Updates the value of an element at a specific index in the linked list.

        Args:
            index: The zero-based index of the element to update.
            value: The new value to set.

        Returns:
            True if the update was successful, False otherwise (e.g., index out of range).
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """
        Inserts a new element (value) at a specific index in the linked list.

        Args:
            index: The zero-based index where to insert the new element.
            value: The value to add to the list.

        Returns:
            True if the insertion was successful, False otherwise (e.g., index out of range).
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """
        Removes the element at a specific index from the linked list.

        Args:
            index: The zero-based index of the element to remove.

        Returns:
            The removed element or None if the index is out of range or the list is empty.
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        """
        Reverses the order of elements in the linked list.

        Modifies the original list in-place.
        """
        if self.length == 0:
            self.head = None
            self.tail = None
            return
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

