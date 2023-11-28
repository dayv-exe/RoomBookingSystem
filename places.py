# THIS MODULE HANDLES PLACES LISTED ON THE APP


class Places:
    def __init__(self):
        # list of valid accommodation types
        self.ACCOMMODATION_TYPES = ["Hotel", "Hostel", "Bed and breakfast", "Apartment", "Guest house", "Dormitory", "Campsite", "Motel", "Cottage", "Resort", "Villa", "Inn", "Chalet", "Lodge", "Homestay", "Log cabin", "Glamping"]

    def valid_accommodation_type(self, user_input):
        # CHECKS IF THE ACCOMMODATION TYPE THE USERS HAS ENTERED CORRESPONDS WITH ANY VALID ACCOM. TYPE
        return False

    def add_new_place(self):
        # prompts user to enter the name, type, and address of a new place they want to add

        # initial prompt to prepare the user
        input("We will need a few details about the place\nlike name, accommodation type, address and cost per night of stay.\nPress enter to continue")
        print("\n")

        # to get a valid name longer than 1 char
        np_name = input("Please enter the name of this new place\n")
        while len(np_name) < 2:
            np_name = input("Please enter a valid name for this new place!\n")

        # to print out a list of valid accommodation types and prompt the user to select
        type_index = 0
        for t in self.ACCOMMODATION_TYPES:
            type_index += 1
            print(f"{type_index}. {t}")
        print(f"What type of place would {np_name} be?")
        np_type = input("*Select accommodation type from menu (enter name or number)*: ")

        np_address = input(f"Where would {np_name} be located?:\n")

        np_price_per_night = input(f"Lastly, how much would {np_name} cost per night:\n")
