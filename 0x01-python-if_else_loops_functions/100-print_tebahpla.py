#!/usr/bin/python3
output = ""
for i in range(ord('z'), ord('a') - 1, -1):
    letter = chr(i)
    case = letter.islower() if i % 2 == 0 else letter.isupper()
    output += case

print(output, end="")
