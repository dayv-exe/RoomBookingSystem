# region SORTING ALGORITHMS
def binary_sort(array, key=None):
    return _sort_array(array, 0, len(array) - 1, key)


def _sort_array(array, start, end, key=None):
    # uses QUICK SORT algorithm to sort an array
    if end > start:
        pivot = _hoare_partition(array, start, end, key)
        _sort_array(array, start, pivot - 1, key)
        _sort_array(array, pivot + 1, end, key)

    return array


def _hoare_partition(array, start, end, key):
    # key allows algorithm to look into values in a dictionary which is what places are stored as
    i = start
    j = end
    pivot = array[(start + end) // 2]
    pivot_ = pivot if key is None else pivot[key]

    def get_array_index(array_index, the_key):
        # to allow hoare partition to be used whether 'key' is provided or not
        return array_index if key is None else array_index[the_key]

    while j > i:

        while get_array_index(array[i], key) < pivot_:
            i += 1

        while get_array_index(array[j], key) > pivot_:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            return j
# endregion
