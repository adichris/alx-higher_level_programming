#!/usr/bin/python3
a = []
for i in range(10):
    for j in range(i+1, 10):
        a.append(f"{i}{j}")

print(*a, sep=', ')
