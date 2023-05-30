#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input or converts numbers. """    
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Try again.")
            continue
    
    number = number * 2
    print("The number is", number)
    
