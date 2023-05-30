#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            num = float(num)
            if num > 0:
                nums.remove(num)
        else:
            print("Invalid input. Try again.")
