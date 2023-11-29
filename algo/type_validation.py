# region TYPE VALIDATION
def is_integer(user_input):
    # returns the user input as an integer if it is a valid integer
    try:
        user_input = int(user_input)
    except ValueError:
        return False

    return user_input
# endregion
