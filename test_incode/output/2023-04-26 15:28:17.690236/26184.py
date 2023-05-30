#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers and stores numbers. """    
    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            number = int(num)
            print(number)
        else:
            print("Invalid input. Try again.")
