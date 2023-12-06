import storage
import random
from functions.sort import quick_sort
from functions.search import binary_search
from classes.place import Place


class Enquiry:
    def __init__(self, enquiry_id):
        self.enquiry_id = enquiry_id

    def _get_self_data(self):
        # uses current enquiry id to get full data on current enquiry
        data = quick_sort(storage.load_data('enquiries'), 'enquiry_id')
        data = binary_search(data, self.enquiry_id, 'enquiry_id')

        return data

    def _enquiry_type(self, accom_name, enquiry, response):
        # to make sure required values are collected for db
        return {
            'enquiry_id': self.enquiry_id,
            'accom_name': accom_name,
            'enquiry': enquiry,
            'response': response
        }

    def _add_to_db(self, accom_name, enquiry):
        # adds new enquiry to db
        new_data = self._enquiry_type(accom_name, enquiry, None)
        storage.save_data(new_data, 'enquiries')

        print("Your query has been submitted, you will receive a response shortly.")

    def _add_response_to_db(self, response):
        # get current enquiry from db
        enquiry_data = self._get_self_data()
        new_data = self._enquiry_type(
            enquiry_data['accom_name'],
            enquiry_data['enquiry'],
            response
        )
        storage.update_data('enquiries', 'enquiry_id', enquiry_data['enquiry_id'], new_data)

        print("Your response has been submitted.")

    @staticmethod
    def make():
        # select place to make enquiry on

        choice = Place.let_user_select("Please enter the number of the place you want to make enquiries on:\n", Place.show_all)
        sel_place = choice['sel_place']

        print(f"You have selected *{sel_place['name'].upper()}*")

        # generates random enquiry id
        enquiry_id = random.randint(1, 999999)
        while binary_search(storage.load_data('enquiries'), search_term=enquiry_id, key='enquiry_id') != -1:
            # if enquiry id already exists
            enquiry_id = random.randint(1, 999999)  # try another random set of numbers

        enquiry = input("Please enter the enquiry you have about this place:\n")

        while len(enquiry) < 3:
            enquiry = input("Please enter a VALID enquiry you have about this place:\n")

        new_enquiry = Enquiry(enquiry_id)
        new_enquiry._add_to_db(sel_place['name'], enquiry)

    def respond(self):
        choice = Place.let_user_select("Please enter the number of the place you want to make enquiries on:\n", Place.show_all)
        sel_place = choice['sel_place']
