# STORES ALL THE DATA STRUCTURE ALGORITHMS TO BE USED IN THE PROJECT

# region TYPE VALIDATION
def is_integer(user_input):
    try:
        user_input = int(user_input)
    except ValueError:
        return False

    return user_input
# endregion

# region SORTING ALGORITHMS
def sort_array(array, start, end):
    # uses QUICK SORT algorithm to sort an array
    if end > start:
        pivot = hoare_partition(array, start, end)
        sort_array(array, start, pivot - 1)
        sort_array(array, pivot + 1, end)

    return array


def hoare_partition(array, start, end):
    i = start
    j = end
    pivot = array[(start + end) // 2]

    while j > i:

        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            return j

# endregion

# region SEARCHING ALGORITHMS


def binary_search(the_list, search_term):
    # returns -1 when no match
    found = False
    found_term_index = -1
    start_index = 0
    end_index = len(the_list) - 1

    while not found and end_index >= start_index:
        midpoint = (start_index + end_index) // 2
        if the_list[midpoint] == search_term:
            found = True
            found_term_index = midpoint

        elif search_term < the_list[midpoint]:
            end_index = midpoint - 1

        else:
            start_index = midpoint + 1

    return found_term_index

# endregion
