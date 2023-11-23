#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list= []
    d = 0
    for a in range(list_length):
        try:
            d =  my_list_1[a] / my_list_2[a]        
        except ZeroDivisionError:
            print("division by 0")
        except (ValueError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(d)
    return new_list