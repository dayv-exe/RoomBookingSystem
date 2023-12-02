# region SORTING ALGORITHMS
def depreciated_sort_array(array, start, end):
    # uses QUICK SORT algorithm to sort an array
    if end > start:
        pivot = _depreciated_hoare_partition(array, start, end)
        depreciated_sort_array(array, start, pivot - 1)
        depreciated_sort_array(array, pivot + 1, end)

    return array


def sort_array(array, start, end, key=None):
    # uses QUICK SORT algorithm to sort an array
    if end > start:
        pivot = _hoare_partition(array, start, end, key)
        sort_array(array, start, pivot - 1, key)
        sort_array(array, pivot + 1, end, key)

    return array


def _hoare_partition(array, start, end, key):
    # key allows algorithm to look into values in a dictionary which is what places are stored as
    i = start
    j = end
    pivot = array[(start + end) // 2]

    def get_array_index(array_index, the_key):
        # to allow hoare partition to be used whether 'key' is provided or not
        return array_index if key is None else array_index[the_key]

    while j > i:

        pivot_ = pivot if key is None else pivot[key]
        while get_array_index(array[i], key) < pivot_:
            i += 1

        pivot_ = pivot if key is None else pivot[key]
        while get_array_index(array[j], key) > pivot_:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            return j


def _depreciated_hoare_partition(array, start, end):
    i = start
    j = end
    pivot = array[(start + end) // 2]

    while j > i:

        while array[i] < pivot:
            # if current item is bigger than pivot
            i += 1

        while array[j] > pivot:
            # if current item is smaller than pivot
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            return j


def filter_places_by(places, search_term, attr='type'):
    # FILTER BY ATTRIBUTE USES HOARE PARTITION TO SORT THE LIST OF PLACES, ATTR COULD BE TYPE, ADDRESS
    # THE HOARE PARTITION THIS TIME IS MODIFIED TO PLACE THE PLACES WITH THE ATTRIBUTE WE ARE LOOKING FOR AT THE START OF THE SORTED LIST

    pass
# endregion
