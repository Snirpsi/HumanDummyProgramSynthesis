#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or multiplyes numbers. """    
    while True:
        num = input("Enter a number: ")
        if num == "exit":
            break
        elif num.isdigit():
            num = float(num)
            print(num * 