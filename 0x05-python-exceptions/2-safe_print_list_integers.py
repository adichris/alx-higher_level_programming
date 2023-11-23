#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for a in my_list[:x]:
        try:
            print("{:d}".format(a), end="", sep="")
            i += 1
        except (TypeError, ValueError):
            pass
    print()
    return i
