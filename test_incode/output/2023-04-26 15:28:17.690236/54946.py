#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers or removes user input. """    
    while True:
        number = input('Enter a number: ')
        if number == 'exit':
            break
        else:
            print(number * 