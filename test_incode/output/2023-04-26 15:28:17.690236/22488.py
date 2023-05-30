#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input or returns a list of numbers. """    
    
    number = input("Enter a number: ")
    
    if number == 'exit':
        sys.exit()
    else:
        print(number)
        
