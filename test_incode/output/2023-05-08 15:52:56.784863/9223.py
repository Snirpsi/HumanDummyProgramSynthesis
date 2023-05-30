#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that requests user input.
    while True:
        print("Enter a number: ")
        number = int(input())
        if number > 100 or number < 0:
            print("Invalid number")
        else:
            break

