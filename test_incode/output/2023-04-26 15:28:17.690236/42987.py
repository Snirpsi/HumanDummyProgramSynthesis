#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or opens numbers. """    
    while True:
        try:
            number = int(input("Enter a number: "))
            if number == -1:
                print("\nExiting...")
                break
            else:
                print("\nThe number is", number)
        except 