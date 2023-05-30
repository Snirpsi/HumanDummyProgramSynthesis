#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or converts a list of words. """    
    while True:
        line = input('Enter a number: ')
        if line == 'q':
            break
        try:
            number = int(line)
        except ValueError:
            print('That is not a number')
        else:
            print(number)
