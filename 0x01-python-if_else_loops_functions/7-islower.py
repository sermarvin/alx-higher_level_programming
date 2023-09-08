#!/usr/bin/python3
def islower(c):
    check = False
    for i in range(97, 123):
        if ord(c) == i:
            check = True
            break
    return(check)
