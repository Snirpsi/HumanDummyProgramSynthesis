#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers or opens a list of words. """    
    while True:
        number = input("Enter a number: ")
        if number == 'exit':
            break
        else:
            print(number)
            
