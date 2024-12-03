def selection_sort(my_list:list):
    """
    Sorts a list of elements in ascending order using the Selection Sort algorithm.

    Selection Sort works by repeatedly finding the smallest element from the unsorted part 
    of the list and swapping it with the first element of the unsorted part.

    Args:
        my_list (list): The list of elements to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    n = len(my_list)

    # Traverse through all elements in the list except the last one
    for current_index in range(n - 1):
        # Assume the current index holds the smallest value
        min_index = current_index

        # Check the rest of the list for a smaller element
        for next_index in range(current_index + 1, n):
            if my_list[next_index] < my_list[min_index]:
                min_index = next_index

        # Swap the smallest element with the first unsorted element
        if current_index != min_index:
            my_list[current_index], my_list[min_index] = my_list[min_index], my_list[current_index]

    return my_list
