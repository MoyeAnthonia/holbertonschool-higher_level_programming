#!/usr/bin/python3

def uniq_add(my_list=[]):
    total_sum = sum({x for x in my_list})
    return total_sum
