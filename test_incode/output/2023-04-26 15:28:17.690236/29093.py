#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input or multiplyes a port. """    
    while True:
        port = int(input('Enter a port number: '))
        if port == -1:
            break
        
        if port % 2 == 0:
            print('Port {} is even.'.format(port))
        else:
            print('Port {} is odd.'.format(port))
            
        print('-' * 80)
        
    print('Program terminated.')
