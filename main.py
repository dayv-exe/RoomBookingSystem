import algo
from places import Places
place = Places()

# CREATE CSV FILES WITH HEADERS FOR STORAGE WHEN PROGRAM IS FIRST RUN (IF FILES DON'T EXIST)
algo.initialize_file(place.PLACES_PATH, f"name, type, address, available_rooms, price")

place.add_new_place()
