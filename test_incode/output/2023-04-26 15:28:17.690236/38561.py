#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input. """    
    while True:
        print("Enter a number:")
        number = int(input())
        if number < 0 or number > 1000:
            print("Invalid number")
        else:
            break
    
    print("The number you entered is {}".format(number))
    
