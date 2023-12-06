# region SORTING ALGORITHMS
def quick_sort(array, key=None):
    # sorting algo entry point
    return _sort_array(array, 0, len(array) - 1, key)


def _sort_array(array, start, end, key=None):
    # uses QUICK SORT algorithm to sort an array

    # key allows algorithm to look into values in a dictionary
    # key is none will compare items in a sorted array, key is not none will compare values in dictionaries in a sorted array
    if end > start:
        pivot = _hoare_partition(array, start, end, key)
        _sort_array(array, start, pivot - 1, key)
        _sort_array(array, pivot + 1, end, key)

    return array


def _hoare_partition(array, start, end, key):
    # key allows algorithm to look into values in a dictionary
    # key is none will compare items in a sorted array, key is not none will compare values in dictionaries in a sorted array
    i = start
    j = end
    pivot = array[(start + end) // 2]
    pivot_val = pivot if key is None else pivot[key]

    def get_array_index(array_index, the_key):
        # return item in an array if no key is provided
        # return value of dictionary if key is provided
        return array_index if key is None else array_index[the_key]

    while j > i:

        if get_array_index(array[i], key) == get_array_index(array[j], key) and i != j:
            next_pos = array.index(array[i]) + 1
            array[next_pos], array[j] = array[j], array[next_pos]

        while get_array_index(array[i], key) < pivot_val:
            i += 1

        while get_array_index(array[j], key) > pivot_val:
            j -= 1

        pivot = array[(start + end) // 2]
        pivot_val = pivot if key is None else pivot[key]

        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            return j
# endregion
