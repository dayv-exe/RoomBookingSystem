def quick_sort(array, key=None):
    # sorting algo entry point
    return _sort_array(array, 0, len(array) - 1, key)


def _sort_array(array, start, end, key=None):
    # uses QUICK SORT algorithm to sort an array
    if end > start:
        pivot = _lomuto_partition(array, start, end, key)
        _sort_array(array, start, pivot - 1, key)
        _sort_array(array, pivot + 1, end, key)

    return array


def _get_array_index(array_index, the_key):
    # return item in an array if no key is provided
    # return value of dictionary if key is provided
    return array_index if the_key is None else array_index[the_key]


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


def _lomuto_partition(array, start, end, key):
    # key allows algorithm to look into values in a dictionary which is what places are stored as
    pivot = array[end]  # selects last item in array as pivot
    pivot_val = pivot if key is None else pivot[key]  # check if key is provided meaning we are sorting dictionaries, key indicates what key in the dictionary algo should sort by

    i = start - 1

    for j in range(start, end):
        if _get_array_index(array[j], key) <= pivot_val:
            # swap and move 1st finger if 2nd finger is less than or equal to pivot
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[end] = array[end], array[i + 1]  # set new pivot pos
    return i + 1
