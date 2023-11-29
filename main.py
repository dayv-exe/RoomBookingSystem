from algo import storage
from places import Places
place = Places()

# CREATE CSV FILES WITH HEADERS FOR STORAGE WHEN PROGRAM IS FIRST RUN (IF FILES DON'T EXIST)
storage.initialize_file(place.PLACES_PATH, place.PLACES_CSV_HEADER)

place.add_new_place()
