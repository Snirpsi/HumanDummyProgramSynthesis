#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input and opens numbers. """    
    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            print(int(num))
        else:
            print("Sorry, that is not a number!")
