#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    while True:
        num = input("Enter a number: ")
        try:
            num = int(num)
        except ValueError:
            print("That is not a number!")
        else:
            if num > 0 and num < 10:
                print(num)
            else:
                print("That is not a number!")
