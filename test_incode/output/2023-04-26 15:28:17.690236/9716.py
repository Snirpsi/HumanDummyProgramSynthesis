#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        number = int(number)
        if number > 0 and number < 10:
            print(number)
        else:
            print("Invalid number")
            
