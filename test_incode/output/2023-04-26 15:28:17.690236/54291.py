#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers or stores numbers. """    
    while True:
        try:
            number = int(input("Enter a number: "))
            if number > 0:
                print("The number you entered is greater than 0")
                