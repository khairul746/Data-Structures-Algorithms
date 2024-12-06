def merge(list1, list2): # Helper function for merge_sort()
    """
    Merges two sorted lists into a single sorted list.

    This function takes two sorted lists and combines them into one sorted list by 
    comparing elements from both lists in ascending order.

    Args:
        list1 (list): The first sorted list.
        list2 (list): The second sorted list.

    Returns:
        list: A merged and sorted list containing all elements from both input lists.
    """
    combined = []  # Initialize the list to store merged elements
    i = 0  # Pointer for list1
    j = 0  # Pointer for list2

    # Compare elements from both lists and append the smaller one
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    # Append any remaining elements from list1
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    # Append any remaining elements from list2
    while j < len(list2):
        combined.append(list2[j])
        j += 1
      
    return combined

def merge_sort(my_list): # Main Function
    """
    Sorts a list in ascending order using the Merge Sort algorithm.

    Merge Sort is a divide-and-conquer algorithm that recursively splits the list
    into smaller sublists, sorts them, and then merges the sorted sublists back together.

    Args:
        my_list (list): The list to be sorted.

    Returns:
        list: A new list that is sorted in ascending order.
    """
    # Base case: A single-element list is already sorted
    if len(my_list) <= 1:
        return my_list

    # Find the middle index to split the list into two halves
    mid_index = len(my_list) // 2

    # Recursively split and sort the left and right halves
    left_half = merge_sort(my_list[:mid_index])
    right_half = merge_sort(my_list[mid_index:])

    # Merge the sorted halves and return the result
    return merge(left_half, right_half)
