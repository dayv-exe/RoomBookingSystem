import json
import os

DATA_PATH = "./data/db.json"
DATA_DIR_PATH = "./data"
EMPTY_DB = {'places': [], 'inquires': [], 'bookings': []}


def test_storage():
    # try reading and writing from the file, if it fails then file is corrupt
    # delete old file and write new one if the user wants to
    try:
        dump_data(load_db())
        return True  # if successful
    except (PermissionError, FileNotFoundError, json.JSONDecodeError) as e:
        print("DATABASE FILE IS CORRUPT!!!")
        user_input = ""
        while user_input.lower() != "y" and user_input.lower() != "n":
            user_input = input("**tip:choose N to see json error message**\nDo you want to clear program cache? (Y/N)\n")

        if user_input.lower() == "y":
            os.remove(DATA_PATH)
            init_db()
            print("Please run the program again.")
        else:
            print(f"JSON ERROR: {e}")

        quit()


def init_db():
    # creates a db.json file and dir if it doesn't already exist

    if not os.path.exists(DATA_DIR_PATH):
        os.makedirs(DATA_DIR_PATH)

    if not os.path.isfile(DATA_PATH):
        with open(DATA_PATH, 'w') as file:
            # Dump the data into the new JSON file
            json.dump(EMPTY_DB, file, indent=2)
    else:
        # if database already exists then check for errors before program starts
        test_storage()


def load_db():
    # loads up the entire db file
    with open(DATA_PATH, 'r') as file:
        data = json.load(file)
        return data


def dump_data(new_data):
    # writes an entire db file
    with open(DATA_PATH, 'w') as file:
        json.dump(new_data, file, indent=2)


def save_data(data, dict_name):
    # Open the JSON file for writing
    new_data = load_db()  # gets json data

    # new_data[dict_name].append(data)
    # region USING LOW QUALITY CODE TO ADD NEW DATA TO EXISTING ARRAY INSTEAD OF 'append()' AS IT IS A BUILT-IN FUNC
    # creates an array 1 length bigger than array loaded frm db and adds all the items from the db array including the new item parsed by user
    new_data_array = [None] * (len(new_data[dict_name]) + 1)
    for i in range(0, len(new_data_array) - 1):
        new_data_array[i] = new_data[dict_name][i]
    new_data_array[len(new_data[dict_name])] = data
    new_data[dict_name] = new_data_array
    # endregion

    dump_data(new_data)  # adds modified data back to json file


def remove_data(dict_name, key, value):
    # Open the JSON file for writing
    new_data = load_db()

    # new_data[dict_name].remove(data)
    # region USING LOW QUALITY CODE TO REMOVE DATA FROM AN EXISTING ARRAY INSTEAD OF 'remove()' AS IT IS A BUILT-IN FUNC
    # creates an array that can be 1 length smaller than array loaded frm db and adds all the items from the db array excluding the item parsed by user
    new_data_array = [None] * (len(new_data[dict_name]))
    current_index = 0
    new_array_size = 0
    for i in new_data[dict_name]:
        # print(f"key {key}, value {value}, found {i.get(key)}")
        if i.get(key) != value:
            new_array_size += 1
            new_data_array[current_index] = i
            current_index += 1

    # sets the old array size to be length of remaining items, then adds each item back to the old array (can not use dynamically sized array as it is built in function)
    new_data[dict_name] = [None] * new_array_size
    for i in range(0, new_array_size):
        new_data[dict_name][i] = new_data_array[i]
    # endregion

    dump_data(new_data)  # adds it back to json file
