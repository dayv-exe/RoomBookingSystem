# region SEARCHING ALGORITHMS


def binary_search(the_list, search_term):
    # uses binary search algorith
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


def binary_search_places(the_list, search_by_index, search_term):
    # uses binary search algorithm to search for places where 'search_by_index' refers to what item in an array of places the algorith should search for
    # e.g. setting the 'search_by_index' to 2 will search for places with address user entered

    # returns -1 when no match
    found = False
    found_term_index = -1
    start_index = 0
    end_index = len(the_list) - 1

    while not found and end_index >= start_index:
        midpoint = (start_index + end_index) // 2
        if the_list[midpoint][search_by_index] == search_term:
            found = True
            found_term_index = midpoint

        elif search_term < the_list[midpoint][search_by_index]:
            end_index = midpoint - 1

        else:
            start_index = midpoint + 1

    return found_term_index


# endregion
