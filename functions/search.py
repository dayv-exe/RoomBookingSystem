# region SEARCHING ALGORITHMS


def binary_search(the_list, search_term, key=None):
    # uses binary search algorith
    # returns -1 when no match
    found = False
    found_term_index = -1
    start_index = 0
    end_index = len(the_list) - 1

    while not found and end_index >= start_index:
        midpoint = (start_index + end_index) // 2
        the_list_midpoint = the_list[midpoint] if key is None else the_list[midpoint][key]
        if the_list_midpoint == search_term:
            found = True
            found_term_index = midpoint

        elif search_term < the_list_midpoint:
            end_index = midpoint - 1

        else:
            start_index = midpoint + 1

    # return found_term_index
    return the_list[found_term_index] if found else -1
# endregion
