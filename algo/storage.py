import csv
import os.path


# region FOR CSV
def initialize_file(file_path, headers):
    # TO CREATE A NEW CSV FILE WITH HEADER
    # only if file does not already exist
    if os.path.isfile(file_path):
        return
    with open(file_path, "w") as file:
        file.write(f"{headers}")


def add_to(file_path, data):
    with open(file_path, "a") as file:
        file.write(f"\n{data}")
# endregion
