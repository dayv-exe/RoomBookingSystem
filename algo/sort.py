# region SORTING ALGORITHMS
def sort_array(array, start, end):
    # uses QUICK SORT algorithm to sort an array
    if end > start:
        pivot = hoare_partition(array, start, end)
        sort_array(array, start, pivot - 1)
        sort_array(array, pivot + 1, end)

    return array


def place_array_sort(array_of_places, sort_by_index, start, end):
    # uses QUICK SORT algorithm to sort an array
    if end > start:
        pivot = hoare_partition_places(array_of_places, sort_by_index, start, end)
        place_array_sort(array_of_places, sort_by_index, start, pivot - 1)
        place_array_sort(array_of_places, sort_by_index, pivot + 1, end)

    return array_of_places


def hoare_partition_places(array_of_places, sort_by_index, start, end):
    # 'sort_by_index' is what item in the array of places should be the focus of the sort
    # e.g. setting the index to 2 will sort by address since address is the 3rd item in array of places
    i = start
    j = end
    pivot = array_of_places[(start + end) // 2]

    while j > i:

        while array_of_places[i][sort_by_index] < pivot[sort_by_index]:
            i += 1

        while array_of_places[j][sort_by_index] > pivot[sort_by_index]:
            j -= 1

        if i < j:
            array_of_places[i], array_of_places[j] = array_of_places[j], array_of_places[i]
        else:
            return j


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
