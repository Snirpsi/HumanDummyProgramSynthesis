#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input or stores numbers. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            print(int(number))
        else:
            print("Invalid input")
