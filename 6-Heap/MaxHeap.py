class MaxHeap:
    """
    Represents a max heap data structure.
    """

    def __init__(self):
        """
        Initializes an empty max heap.
        """
        self.heap = []

    def _left_child_index(self, index):
        """
        Calculates the index of the left child of a given node.

        Args:
            index: The index of the parent node.

        Returns:
            The index of the left child.
        """
        return 2 * index + 1

    def _right_child_index(self, index):
        """
        Calculates the index of the right child of a given node.

        Args:
            index: The index of the parent node.

        Returns:
            The index of the right child.
        """
        return 2 * index + 2

    def _parent_index(self, index):
        """
        Calculates the index of the parent of a given node.

        Args:
            index: The index of the child node.

        Returns:
            The index of the parent node.
        """
        return (index - 1) // 2

    def _swap(self, index1, index2):
        """
        Swaps two elements in the heap.

        Args:
            index1: The index of the first element.
            index2: The index of the second element.
        """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        """
        Inserts a new value into the max heap.

        Args:
            value: The value to insert.
        """
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent_index(current)]:
            self._swap(current,   
 self._parent_index(current))
            current = self._parent_index(current)

    def _sink_down(self, index):
        """
        Restores the max heap property by moving the element at the given index down to its correct position.

        Args:
            index: The index of the element to sink down.
        """
        max_index = index
        while True:
            left_index = self._left_child_index(max_index)
            right_index = self._right_child_index(max_index)

            if left_index < len(self.heap) and self.heap[max_index] < self.heap[left_index]:
                max_index = left_index
            if right_index < len(self.heap) and self.heap[max_index] < self.heap[right_index]:
                max_index = right_index
            if max_index != index:
                self._swap(max_index, index)
                index = max_index
            else:
                return

    def remove(self):
        """
        Removes and returns the maximum value from the heap.

        Returns:
            The maximum value, or None if the heap is empty.
        """
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value

myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)


myheap.remove()

print(myheap.heap)


myheap.remove()

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [95, 75, 80, 55, 60, 50, 65]
    [80, 75, 65, 55, 60, 50]
    [75, 60, 65, 55, 50]

"""
