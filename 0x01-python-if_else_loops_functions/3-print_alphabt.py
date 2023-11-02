#!/usr/bin/python3
for a in list('abcdefghijklmnopqrstuvwxyz'):
    if a == 'q' or a == 'e':
        continue
    print('{a}'.format(a=a), end="")
