#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == 'done':
            break
        number = int(number)
        print(number)
        
