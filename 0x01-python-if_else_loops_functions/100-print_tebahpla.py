#!/usr/bin/python3
for char_code in range(ord('z'), ord('a') - 1, -1):
    char = chr(char_code)
    if char.islower():
        print(char, end='')
    elif char.isupper():
        print(char, end=' ')

