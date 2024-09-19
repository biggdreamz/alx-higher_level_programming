#!/usr/bin/python3

# Use a set to store unique integers and sum them

def uniq_add(my_list=[]):
    unique_int = set(my_list)
    return sum(unique_int)
