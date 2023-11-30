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


def binary_search_places(the_list, search_term="", key=""):
    # uses binary search algorith
    # returns -1 when no match
    # key allows algorithm to lok into values in a dictionary which is what places is stored as
    found = False
    found_term_index = -1
    start_index = 0
    end_index = len(the_list) - 1

    search_term = search_term.lower()

    while not found and end_index >= start_index:
        midpoint = (start_index + end_index) // 2
        if the_list[midpoint][key].lower() == search_term:
            found = True
            found_term_index = midpoint

        elif search_term < the_list[midpoint][key].lower():
            end_index = midpoint - 1

        else:
            start_index = midpoint + 1

    return found_term_index

# endregion
