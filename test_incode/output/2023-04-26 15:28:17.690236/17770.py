#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers and iterates over words. """    
    while True:
        number = int(input('Enter a number: '))
        word = ''.join(str(n) for n in range(number))
        print('The number {} is a {}'.format(number, word))
        
        if number == 0: break
        
