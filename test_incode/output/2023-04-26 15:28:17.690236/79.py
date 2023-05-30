#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input or enumerates a list of numbers. """    
    
    while True:
        num = input("Enter a number: ")
        if num == 'q':
            break
        else:
            print(num)
            
