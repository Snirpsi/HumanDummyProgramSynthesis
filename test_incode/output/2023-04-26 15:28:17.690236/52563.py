#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or returns user input. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            number = int(number)
            if number > 0 and number <= 10:
                numbers.append(number)
            else:
                print("Invalid number")
        else:
            print("Invalid number")
    
