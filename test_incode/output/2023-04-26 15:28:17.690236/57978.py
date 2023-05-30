#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input or converts numbers. """    
    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            print(int(num))
        else:
            print("Not a number")
