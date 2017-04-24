#!/usr/bin/env python

global global_variable = 6

def test_data_function():

    new_string = raw_input(" new character ")

    if new_string == 'm':
        global_variable = global_variable - 1
    else:
        print "You didnt push m"

    return new_string

#### main

print "Begin function"
print global_variable
this_string = test_data_function()
print global_variable