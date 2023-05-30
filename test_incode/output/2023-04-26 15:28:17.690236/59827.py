#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or iterates over a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("Invalid input. Please try again.")
        else:
            if number > 0 and number < 10:
                print("The number you entered is {}.".format(number))
            else:
                print("The number you entered is out of range. Please try again.")
        
