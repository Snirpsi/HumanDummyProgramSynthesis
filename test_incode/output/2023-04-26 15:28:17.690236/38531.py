#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input and adds a list of numbers. """    
    
    while True:
        answer = input('Enter a number: ')
        try:
            answer = float(answer)
        except ValueError:
            print('That is not a number!')
        else:
            print('The number is', answer)
            
