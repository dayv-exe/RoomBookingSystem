import storage
from functions.sort import quick_sort


def db_id(dict_name, id_key):
    # returns an id, a number one higher than the number of the previous item in database
    # e.g. if a db is empty, will return 1, else the the last item in the db has id of 3 then will return 4

    stored_items = storage.load_data(dict_name)
    if len(stored_items) < 1:
        return 1

    stored_items = quick_sort(stored_items, id_key)
    last_id = int(stored_items[len(stored_items) - 1][id_key])

    return last_id + 1
