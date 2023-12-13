# region TYPE VALIDATION
def is_integer(user_input, num_range=None):
    # this functions checks if input parsed is is an integer within range of num_range parsed
    # i.e. user_input=3, num_range=[1, 5] will return True since 3 is a num and it is between range
    # returns the user input as an integer if it is a valid integer
    # num_range should be an array of 2 numbers the first being the smallest acceptable from user and the last being the largest num acceptable from user
    try:
        user_input = int(user_input)
    except ValueError:
        return False

    if num_range is not None:
        # returns false if the number is an integer but does not fall within required range
        return user_input if num_range[0] <= user_input <= num_range[1] else False

    return user_input
# endregion
