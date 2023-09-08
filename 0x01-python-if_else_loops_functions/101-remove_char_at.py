#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    for char in range(len(str)):
        if char == n:
            continue
        new_string += str[char]
    return (new_string)
