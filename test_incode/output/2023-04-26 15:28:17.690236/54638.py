#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers. """    
    while True:
        num = input("Enter a number: ")
        num = num.strip()
        num = num.lower()
        if num.isdigit():
            num = int(num)
            print(num)
        else:
            print("Invalid input.")
