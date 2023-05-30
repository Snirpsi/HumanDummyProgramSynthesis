#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            num = num.strip()
            if num.isdigit():
                num = float(num)
                if num > 0 and num < 10:
                    num = num