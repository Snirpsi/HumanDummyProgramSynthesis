#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            num = int(num)
            if num > 0 and num < 10:
                print(num)
            else:
                print("Invalid number")
        else:
            print("Invalid number")
