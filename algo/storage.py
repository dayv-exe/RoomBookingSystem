import csv
import os.path
from algo import sort


def initialize_file(file_path, headers):
    # TO CREATE A NEW CSV FILE WITH HEADER
    # only if file does not already exist
    if os.path.isfile(file_path):
        return
    with open(file_path, "w") as file:
        file.write(f"{headers}")


def append_data(file_path, data):
    # to add a new line to csv file
    with open(file_path, "a") as file:
        file.write(f"\n{data}")


def sort_places(file_path, sort_by_index=0):
    # 'sort_by_index' is what item in the array of places should be the focus of the sort
    # e.g. setting the index to 2 will sort by address since address is the 3rd item in array of places
    # and setting it to 0 will sort by name since name is the first item in the array of places
    if not os.path.isfile(file_path):
        return []
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # ignore header
        a = []
        for line in csv_reader:
            a.append(line)

        return sort.place_array_sort(a, sort_by_index, 0, len(a) - 1)
