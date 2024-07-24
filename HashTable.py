class HashTable:
    """
    Represents a hash table data structure.
    """

    def __init__(self, size=7):
        """
        Initializes a new hash table with the specified size.

        Args:
            size: The initial size of the hash table (default: 7).
        """
        self.data_map = [None] * size

    def __hash(self, key):
        """
        Calculates the hash value for a given key.

        Args:
            key: The key to hash.

        Returns:
            The calculated hash value.
        """
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        """
        Prints the contents of the hash table for debugging purposes.
        """
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        """
        Sets a key-value pair in the hash table.

        Args:
            key: The key to associate with the value.
            value: The value to store.
        """
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        """
        Retrieves the value associated with a given key.

        Args:
            key: The key to search for.

        Returns:
            The value associated with the key, or None if not found.
        """
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        """
        Returns a list of all keys in the hash table.
        """
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
