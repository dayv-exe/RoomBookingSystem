# STORES ALL THE DATA STRUCTURE ALGORITHMS TO BE USED IN THE PROJECT
import string


class LinearHashTable:
    def __init__(self, num_of_buckets):
        self.num_of_buckets = num_of_buckets
        self.buckets = [None] * self.num_of_buckets

    @staticmethod
    def calc_hash(key):
        hash_code = 0

        current_index = 0
        for c in key:
            hash_code += string.ascii_lowercase.index(c.lower()) * (31 ** current_index)
            current_index += 1

        return hash_code

    @staticmethod
    def calc_secondary_hash(hashed_key):
        return hashed_key % 17

    def put(self, key, value):
        # adds new item to table
        keyval = (key, value)
        bucket_index = self.calc_hash(key) % self.num_of_buckets
        if self.buckets[bucket_index] is not None:
            bucket_index = self.calc_secondary_hash(bucket_index)
            while self.buckets[bucket_index] is not None:
                if bucket_index >= len(self.buckets):
                    bucket_index = bucket_index % len(self.buckets)
                else:
                    bucket_index += 1
        self.buckets[bucket_index] = keyval

    def get(self, key):
        # returns value by key
        bucket_index = self.calc_hash(key) % self.num_of_buckets
        while self.buckets[bucket_index][0] is not key:
            if bucket_index == len(self.buckets):
                bucket_index = 0
            else:
                bucket_index += 1

    def __str__(self):
        return f"Linear probing table: {self.buckets.__str__()}"

def search_str_array(the_array, search_str):
    # TO SEARCH AN ARRAY OF STRINGS.
    # returns a match when found, returns None if false

    # hash the array then use binary search



    return None
