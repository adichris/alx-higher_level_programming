#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for x in my_list[:x]:
            i += 1
            print(x, sep="", end="")
    except ValueError:
        i += 1
    else:
        print()
        return i
