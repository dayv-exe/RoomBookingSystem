# region SORTING ALGORITHMS
def sort_array(array, start, end):
    # uses QUICK SORT algorithm to sort an array
    if end > start:
        pivot = _hoare_partition(array, start, end)
        sort_array(array, start, pivot - 1)
        sort_array(array, pivot + 1, end)

    return array


def sort_places_array(array, key, start, end):
    # uses QUICK SORT algorithm to sort an array
    # key allows algorithm to lok into values in a dictionary which is what places is stored as
    if end > start:
        pivot = _hoare_partition_places(array, key, start, end)
        sort_places_array(array, key, start, pivot - 1)
        sort_places_array(array, key, pivot + 1, end)

    return array


def _hoare_partition_places(array, key, start, end):
    # key allows algorithm to lok into values in a dictionary which is what places is stored as
    i = start
    j = end
    pivot = array[(start + end) // 2]

    while j > i:

        while array[i][key] < pivot[key]:
            i += 1

        while array[j][key] > pivot[key]:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            return j


def _hoare_partition(array, start, end):
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
