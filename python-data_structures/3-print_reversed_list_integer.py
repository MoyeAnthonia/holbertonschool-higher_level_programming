#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list == []:
        return None

    my_list.reverse()
    print("{:d}".format(my_list))
    return my_list
