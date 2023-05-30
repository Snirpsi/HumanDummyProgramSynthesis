#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input and enumerates numbers. """    
    
    while True:
        number = input("Enter a number: ")
        number = int(number)
        
        if number == 999:
            break
        
        print(number)
        
