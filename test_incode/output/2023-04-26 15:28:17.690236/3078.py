#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or opens fruits. """    
    while True:
        number = input("Enter a number or type 'quit' to quit: ")
        if number == "quit":
            break
        else:
            print(number)
            
