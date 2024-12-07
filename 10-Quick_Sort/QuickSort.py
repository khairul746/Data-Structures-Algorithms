def swap(my_list, index1, index2):
    """
    Swaps the elements at two specified indices in a list.

    Args:
        my_list (list): The list containing elements to swap.
        index1 (int): The index of the first element.
        index2 (int): The index of the second element.
    """
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    """
    Rearranges elements around a pivot in a list.

    The pivot is the element at `pivot_index`. Elements smaller than the pivot
    are moved to its left, and elements larger than the pivot are moved to its right.

    Args:
        my_list (list): The list to partition.
        pivot_index (int): The index of the pivot element.
        end_index (int): The last index to consider in the list.

    Returns:
        int: The final position of the pivot element after partitioning.
    """
    # Initial index where smaller elements will be placed
    swap_index = pivot_index

    # Compare each element with the pivot
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)

    # Move the pivot to its correct position
    swap(my_list, pivot_index, swap_index)

    return swap_index

def quick_sort_helper(my_list, left, right):
    """
    Recursively sorts a portion of a list using the Quick Sort algorithm.

    This function partitions the list around a pivot element, recursively sorts
    the sublists to the left and right of the pivot, and returns the sorted list.

    Args:
        my_list (list): The list to be sorted.
        left (int): The starting index of the portion to sort.
        right (int): The ending index of the portion to sort.

    Returns:
        list: The partially or fully sorted list.
    """
    if left < right:
        # Partition the list and get the index of the pivot
        pivot_index = pivot(my_list, left, right)

        # Recursively sort the left sublist
        quick_sort_helper(my_list, left, pivot_index - 1)

        # Recursively sort the right sublist
        quick_sort_helper(my_list, pivot_index + 1, right)

    return my_list


def quick_sort(my_list):
    """
    Sorts a list in ascending order using the Quick Sort algorithm.

    Args:
        my_list (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    # Call the recursive helper function with the full list range
    return quick_sort_helper(my_list, 0, len(my_list) - 1)
