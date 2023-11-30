# region SORTING ALGORITHMS
def sort_array(array, start, end):
    # uses QUICK SORT algorithm to sort an array
    if end > start:
        pivot = hoare_partition(array, start, end)
        sort_array(array, start, pivot - 1)
        sort_array(array, pivot + 1, end)

    return array


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
