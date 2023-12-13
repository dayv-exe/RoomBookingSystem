from functions.array import append


# region SEARCHING ALGORITHMS
def check_right_neighbour(the_list, current_index, search_term, key=None):
    return check_neighbour(the_list, current_index, search_term, 1, key, [])


def check_left_neighbour(the_list, current_index, search_term, key=None):
    return check_neighbour(the_list, current_index, search_term, -1, key, [])


def check_neighbour(the_list, current_index, search_term, move, key=None, found=None):
    # to enable this version of binary search algo to return multiple results
    # this func checks to see if the item left or right of the item in current index matches the search term provided
    # since the array to be search will be sorted, all the duplicate items will be next to each other
    # this func will check the neighbor of the item we are looking for to see if the neighbor is a duplicate of the search item and can return an array of all duplicates as a result

    if found is None:
        found = []
    if current_index + move < 0 or current_index + move > (len(the_list) - 1):
        # if it is at end of list
        return None

    neighbor_item = the_list[current_index + move] if key is None else the_list[current_index + move][key]
    if neighbor_item == search_term:
        # if neighbour is duplicate add to array
        check_neighbour(the_list, current_index + move, search_term, move, key, found)
        # found.append(the_list[current_index + move])
        found = append(found, the_list[current_index + move])
        return found
    else:
        return None


def binary_search(the_list, search_term, key=None, return_mult_results=False):
    # uses binary search algorith
    # returns -1 when no match
    found = False
    found_term_index = -1
    found_items = []
    start_index = 0
    end_index = len(the_list) - 1

    while not found and end_index >= start_index:
        midpoint = (start_index + end_index) // 2
        the_list_midpoint = the_list[midpoint] if key is None else the_list[midpoint][key]
        if the_list_midpoint == search_term:
            # to be able to return more than one result:
            # allow the algorithm to recursively compare the items to the left or right of the found term
            # only check immediate item to the left or to the right, if the immediate item is a match then check the other immediate items until no more matches are found
            found = True
            found_term_index = midpoint
            found_left = check_left_neighbour(the_list, midpoint, search_term, key)
            found_right = check_right_neighbour(the_list, midpoint, search_term, key)

            # found_items.append(the_list[found_term_index])
            found_items = append(found_items, the_list[found_term_index])
            if found_left is not None:
                for item in found_left:
                    # found_items.append(item)
                    found_items = append(found_items, item)

            if found_right is not None:
                for item in found_right:
                    # found_items.append(item)
                    found_items = append(found_items, item)

        elif search_term < the_list_midpoint:
            end_index = midpoint - 1

        else:
            start_index = midpoint + 1

    # return the_list[found_term_index] if found else -1
    return (found_items[0] if not return_mult_results else found_items) if len(found_items) > 0 else -1
# endregion
