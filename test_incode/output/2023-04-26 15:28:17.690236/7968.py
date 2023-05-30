#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers or stores numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        else:
            print(number)
            