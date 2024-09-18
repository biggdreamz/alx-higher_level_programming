#!/usr/bin/python3

# Create a new list with replaced elements

def search_replace(my_list, search, replace):
    return [replace if element == search else element for element in my_list]
