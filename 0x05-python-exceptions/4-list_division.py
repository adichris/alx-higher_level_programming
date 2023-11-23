#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list= []
    try:
        for a in range(list_length):
            d =  my_list_1[a] / my_list_2[a]
            new_list.append(d)
    except ZeroDivisionError:
        print("division by 0")
    except ValueError:
        print("wrong type")
    except IndexError:
        print("out of range")
    finally:
        return new_list
