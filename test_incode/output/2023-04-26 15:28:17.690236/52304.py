#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers and stores words. """    
    words = []
    while True:
        number = int(input('Enter a number: '))
        if number == 0:
            break
        words.append(str(number))
    print('\n'.join(words))
