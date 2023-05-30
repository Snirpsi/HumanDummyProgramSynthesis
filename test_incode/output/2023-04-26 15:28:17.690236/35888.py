#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words or enumerates numbers. """    
    
    words = []
    
    while True:
        try:
            number = int(input('Enter a number: '))
            words.append(number)
        except ValueError:
            print('Invalid input')
            continue
        else:
            break
    
    print('\n'.join(words))
    
