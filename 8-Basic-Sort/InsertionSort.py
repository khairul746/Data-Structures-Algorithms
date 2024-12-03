def insertion_sort(my_list):
    """
    Sorts a list of elements in ascending order using the Insertion Sort algorithm.

    Insertion Sort works by building a sorted portion of the list one element at a time.
    Each element is compared with elements in the sorted portion and inserted in its correct position.

    Args:
        my_list (list): The list of elements to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    # Start from the second element (index 1) since a single-element list is already sorted
    for current_index in range(1, len(my_list)):
        # Store the current value to be inserted into the sorted portion
        current_value = my_list[current_index]
        # Initialize the previous index
        previous_index = current_index - 1

        # Shift elements of the sorted portion to the right to make space for the current value
        while previous_index >= 0 and current_value < my_list[previous_index]:
            my_list[previous_index + 1] = my_list[previous_index]
            my_list[previous_index] = current_value
            previous_index -= 1

    return my_list
