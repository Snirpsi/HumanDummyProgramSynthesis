#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port and adds words. """    
    port = int(input('Enter a port number: '))
    words = []
    
    for x in range(1, port+1):
        words.append(str(x))
    
    words.append('end')
    
    print('\n'.join(words))
    
