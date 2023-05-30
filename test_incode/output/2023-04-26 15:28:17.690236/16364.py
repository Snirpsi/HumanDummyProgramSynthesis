#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers or prints numbers. """    
    while True:
        print("Enter a number:")
        number = int(input())
        if number % 2 == 0:
            print(number)
        else:
            break
        
