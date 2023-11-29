# region TYPE VALIDATION
def is_integer(user_input):
    try:
        user_input = int(user_input)
    except ValueError:
        return False

    return user_input
# endregion
