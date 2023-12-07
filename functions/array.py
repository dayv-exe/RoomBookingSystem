# USING LOW QUALITY CODE TO ADD OR REMOVE DATA TO EXISTING ARRAY INSTEAD OF 'append()' OR 'remove()' AS IT IS A BUILT-IN FUNC

def append(array, new_item):
    new_array = [None] * (len(array) + 1)
    cur_index = 0
    for i in array:
        new_array[cur_index] = i
        cur_index += 1
    new_array[len(array)] = new_item
    return new_array


def remove(array, item, key=None):
    new_array = [None] * (len(array) - 1)
    curr_index = 0
    found = False
    for i in array:
        cur_item = i[key] if key is not None else i
        if cur_item == item:
            found = True
        else:
            new_array[curr_index] = i
            curr_index += 1

    return new_array if found else array
