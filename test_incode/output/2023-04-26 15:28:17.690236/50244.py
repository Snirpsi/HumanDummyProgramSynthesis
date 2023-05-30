#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            num = float(num)
            if num > 0:
                print("The number you entered is {}".format(num))
                num = int(num)
            else:
                print("The number you entered is {}".format(num))
        else:
            print("Please only enter numbers.")
