#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            num = int(num)
            if num > 0:
                print(num)
            else:
                print("Sorry, that number is too small.")
        else:
            print("Sorry, that is not a valid number.")
