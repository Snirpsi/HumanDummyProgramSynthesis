#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            print(int(number))
        else:
            break

<|/ file source=github |>