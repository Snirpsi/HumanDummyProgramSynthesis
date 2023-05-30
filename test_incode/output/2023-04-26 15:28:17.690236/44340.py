#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words or multiplyes numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == "exit":
            break
        elif number.isdigit():
            print(number * 2)
        else:
            print(number * 