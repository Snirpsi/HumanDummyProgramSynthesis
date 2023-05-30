#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input and multiplyes numbers. """    
    while True:
        num = input("Enter a number: ")
        try:
            num = float(num)
        except ValueError:
            print("Invalid number. Try again.")
            continue
        else:
            print("The product is", num * num)
            break
