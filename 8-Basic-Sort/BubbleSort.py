def bubble_sort(my_list):
    """
    Sorts a list of elements in ascending order using the Bubble Sort algorithm.

    Bubble Sort works by repeatedly swapping adjacent elements if they are in the wrong order.
    The largest elements "bubble up" to the end of the list in each pass.

    Args:
        my_list (list): The list of elements to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    # Perform passes over the list, reducing the range with each iteration
    n = len(my_list)
    for pass_index in range(n - 1, 0, -1):
        # Iterate through the unsorted part of the list
        for current_index in range(pass_index):
            # Swap adjacent elements if they are out of order
            if my_list[current_index] > my_list[current_index + 1]:
                my_list[current_index], my_list[current_index + 1] = (
                    my_list[current_index + 1],
                    my_list[current_index],
                )
    return my_list
  
if __name__ = "__main__":
    # Example list to sort
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]

    # Perform Bubble Sort
    sorted_list = bubble_sort(unsorted_list)

    # Print the sorted and unsorted list
    print("un-Sorted List:", unsorted_list) # Output: [64, 34, 25, 12, 22, 11, 90]
    print("Sorted List:", sorted_list)  # Output: [11, 12, 22, 25, 34, 64, 90]
