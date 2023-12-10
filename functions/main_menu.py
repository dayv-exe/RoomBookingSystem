from functions.type_validation import is_integer
from classes.place import Place
from classes.enquiry import Enquiry
from classes.booking import Booking


def show():
    print(f'*** MAIN MENU ***')
    print(f'[Enter 1 to book a place to stay.]')
    print(f'[Enter 2 to make an enquiry.]')
    print(f'[Enter 3 for routing.]')
    print(f'[Enter 4 to show all places.]')
    print(f'[Enter 5 to search for a place.]')
    print('')
    print(f'[Enter 6 for more options.]')

    sel = input('')
    while not is_integer(sel, [1, 6]):
        sel = input('enter valid option: ')

    sel = int(sel)
    if sel == 6:
        show_advanced()
    elif sel == 1:
        Booking.make()
        _return_to_main_menu_prompt()
    elif sel == 2:
        Enquiry.make()
        _return_to_main_menu_prompt()
    elif sel == 3:
        print("Nothing to see here!")
        _return_to_main_menu_prompt()
    elif sel == 4:
        Place.show_all()
        _return_to_main_menu_prompt()
    elif sel == 5:
        show_search_menu()


def show_advanced():
    print(f'\n*** MORE OPTIONS ***')
    print(f'[Enter 11 to create a new place.]')
    print(f'[Enter 12 to respond to an enquiry.]')
    print(f'[Enter 13 to end a bookings.]')
    print(f'[Enter 14 to view all bookings.]')
    print(f'[Enter 15 to view all enquiries.]')

    sel = input('')
    while not is_integer(sel, [11, 15]):
        sel = input('enter valid option: ')

    sel = int(sel)
    if sel == 11:
        Place.create()
        _return_to_main_menu_prompt()
    elif sel == 12:
        Enquiry.respond()
        _return_to_main_menu_prompt()
    elif sel == 13:
        Booking.end()
        _return_to_main_menu_prompt()
    elif sel == 14:
        Booking.show_all()
        _return_to_main_menu_prompt()
    elif sel == 15:
        Enquiry.show_all()
        _return_to_main_menu_prompt()


def show_search_menu():
    print(f'\n*** SEARCH MENU ***')
    print(f'[Enter 21 to search for places by id.]')
    print(f'[Enter 22 to search for places by type.]')
    print(f'[Enter 23 to search for places by name and address.]')

    sel = input('')
    while not is_integer(sel, [21, 22]):
        sel = input('enter valid option: ')

    sel = int(sel)
    if sel == 21:
        Place.search()
        _return_to_main_menu_prompt()
    elif sel == 22:
        Place.search_by_type()
        _return_to_main_menu_prompt()


def _return_to_main_menu_prompt():
    input('\n[press enter to return to main menu]\n')
