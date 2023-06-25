#!/usr/bin/env python3

from hash_table import HashTable

class QuadraticProbing(HashTable):
    """
    Basic Hash Table example with open addressing using Quadratic Probing
    """

    def __init__(self, *args, c_1: float = None, c_2: float= None, **kwargs):
        super().__init__(*args, **kwargs)
        self.c_1 = c_1
        self.c_2 = c_2

    def hash_function(self, key):
        #edit this function to change the hash function
        return (key + 3) % 11

    def _collision_resolution(self, key, data=None):
        i = 1
        new_key = self.hash_function(data)

        while self.values[new_key] is not None and self.values[new_key] != data:
            # print(f"data = {data}\n"
            #       f"(self.hash_function(data) + (self.c_1 * i) + (self.c_2 * i * i)) % self.size_table  | i {i}\n"
            #       f"({self.hash_function(data)}+ {self.c_1 * i} + {self.c_2 * i * i}) % {self.size_table} = {(self.hash_function(data) + (self.c_1 * i) + (self.c_2 * i * i)) % self.size_table}")
            new_key = (
                (self.hash_function(data) + (self.c_1 * i) + (self.c_2 * i * i)) % self.size_table
                if not self.balanced_factor() >= self.lim_charge
                else None
            )
            i += 1

            if new_key is None:
                break

        return new_key


if __name__ == '__main__':
    #REMEMBER TO CHANGE THE HASH FUNCTION IN THE CLASS
    q_hash = QuadraticProbing(11, values=[13, 39, None, 36, None, None, None, None, 23, 5, None], c_1=3, c_2=1)
    # for n in [13, 39, 36, 23, 5]:
    #     q_hash.insert_data(n)

    q_hash.insert_data(22)
    q_hash.insert_data(16)
    q_hash.insert_data(17)

    print(q_hash)