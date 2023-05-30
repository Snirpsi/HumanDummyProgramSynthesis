#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and enumerates numbers. """    
    while True:
        print("Enter a number: ")
        number = input()
        
        if number == 'q':
            break
        else:
            print(number)
            
