#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input or adds numbers. """    
    
    while True:
        number = int(input('Enter a number: '))
        if number == -1:
            break
        else:
            print(number)
            
    print('Done!')
    
