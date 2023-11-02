#!/usr/bin/python3
def uppercase(str):
   for a in str:
       char = ord(a)
       if char >= 97 and char <= 122:
           print(f"{chr(char-32)}", end="")
       else:
           print(a, end="")
    print()

       
