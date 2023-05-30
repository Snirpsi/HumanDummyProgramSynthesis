#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words or converts a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['1', '2', '3']
    
    numbers = []
    for word in words:
        try:
            number = int(word)
        except ValueError:
            print('Invalid number: ' + word)
        else:
            numbers.append(number)
    
    numbers = map(lambda x: x*2, numbers)
    
    print('\n'.join(map(str, numbers)))
    
