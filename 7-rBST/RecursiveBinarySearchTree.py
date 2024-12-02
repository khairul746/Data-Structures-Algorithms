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
        r_insert(value): Public method to recursively insert a value into the tree.
        r_contains(value) : Recursively checks if a value exists in the tree.
        min_value(current_node) : Finds the minimum value starting from the given node.
        delete_node(value) : Delete a node with the specified value from the tree.
        breadth_first_search(): Performs a breadth-first search (BFS) on the tree and returns the values in level-order.
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

    def __r_contains(self, current_node, value):
        """
        Recursively checks if a value exists in the tree starting from the given node.

        Args:
            current_node (Node): The current node being checked.
            value: The value to search for in the tree.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        # If the node is None, the value does not exist in the tree
        if current_node == None:
            return False

        # Traverse the left subtree if the value is smaller
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)

        # Traverse the right subtree if the value is larger
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

        # If the value matches the current node's value, return True
        if value == current_node.value:
            return True
            
    def r_contains(self,value):
        """
        Checks if a value exists in the binary search tree.

        Args:
            value: The value to search for in the tree.

        Returns:
            bool: True if the value exists in the tree, False otherwise.
        """
        return self.__r_contains(self.root,value)

    def min_value(self, current_node):
        """
        Finds the minimum value in the binary search tree starting from the given node.

        The minimum value in a binary search tree is located in the leftmost node.

        Args:
            current_node (Node): The node to start the search from.

        Returns:
            value: The minimum value in the subtree.
        """
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        """
        Recursively deletes a node with the specified value from the subtree rooted at the given node.

        Args:
            current_node (Node): The current node being checked.
            value: The value to delete from the tree.

        Returns:
            Node: The updated subtree after the deletion.
        """
        # Base case: If the node is None, the value is not in the tree
        if current_node is None:
            return None

        # Traverse the left subtree if the value is smaller
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)

        # Traverse the right subtree if the value is larger
        if value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)

        # If the value matches the current node's value
        else: 
            # Case 1: No children (leaf node)
            if current_node.left is None and current_node.right is None:
                return None

            # Case 2: Only one child (left child exists)
            elif current_node.right is None:
                return current_node.left

            # Case 3: Only one child (right child exists)
            elif current_node.left is None:
                return current_node.right

            # Case 4: Two children
            else:
                # Find the minimum value in the right subtree
                sub_tree_min = self.min_value(current_node.right)
                # Replace the current node's value with the minimum value
                current_node.value = sub_tree_min
                # Delete the duplicate node in the right subtree
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
                
        return current_node
        
    def delete_node(self, value):
        """
        Deletes a node with the specified value from the binary search tree.

        Args:
            value: The value to delete from the tree.
        """
        self.__delete_node(self.root, value)

    def breadth_first_search(self):
        """
        Performs a breadth-first search (BFS) traversal on the binary tree.

        BFS visits each level of the tree one at a time, starting from the root.

        Returns:
            list: A list of node values in BFS order.
        """
        # If the tree is empty, return an empty list
        if self.root is None:
            return []

        # Initialize the queue and the results list
        queue = [self.root]  # Start with the root node in the queue
        results = []

        # Traverse the tree level by level
        while queue:
            # Dequeue the first node in the queue
            current_node = queue.pop(0)
            # Add the current node's value to the results list
            results.append(current_node.value)

            # Enqueue the left child if it exists
            if current_node.left is not None:
                queue.append(current_node.left)

            # Enqueue the right child if it exists
            if current_node.right is not None:
                queue.append(current_node.right)

        return results
        
    def dfs_pre_order(self):
        """
        Performs a depth-first search (DFS) pre-order traversal on the binary tree.

        Pre-order traversal visits nodes in the following order:
        1. Visit the current node.
        2. Traverse the left subtree.
        3. Traverse the right subtree.

        Returns:
            list: A list of node values in pre-order traversal order.
        """
        results = []

        def traverse(current_node):
            """
            Recursively traverses the tree in pre-order.

            Args:
                node (Node): The current node being visited.
            """
            if current_node is None:
                return
            
            # Visit the current node
            results.append(current_node.value)
            
            # Traverse the left subtree
            if current_node.left is not None:
                traverse(current_node.left)
            
            # Traverse the right subtree
            if current_node.right is not None:
                traverse(current_node.right)

        # Start traversal from the root node
        traverse(self.root)
        return results

# Example usage
if __name__ == "__main__":
    # Create a binary tree and insert values
    tree = BinarySearchTree()
    tree.r_insert(10)
    tree.r_insert(5)
    tree.r_insert(15)
    tree.r_insert(2)
    tree.r_insert(7)
    
    # Delete a node with a specific value
    tree.delete_node(5)
    
    # Verify the tree structure
    print(tree.r_contains(5))  # Output: False

    # Perform BFS traversal
    bfs_result = tree.breadth_first_search()
    print("BFS Traversal:", bfs_result)  # Output: [10, 5, 15, 2, 7]

    # Perform DFS Pre-Order traversal
    dfs_result = tree.dfs_pre_order()
    print("DFS Pre-Order Traversal:", dfs_result)  # Output: [10, 5, 2, 7, 15]
