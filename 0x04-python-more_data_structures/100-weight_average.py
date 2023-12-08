#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    denci = 0

    for tup in my_list:
        number += tup[0] * tup[1]
        denci += tup[1]

    return (number / denci)
