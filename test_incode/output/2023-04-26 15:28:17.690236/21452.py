#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input and multiplyes a port. """    
    while True:
        port = int(input('Enter a port number: '))
        
        print('Enter a number: ')
        num = int(input())
        
        print('Multiplying {} by {} is {}'.format(num, port, num*port))
        
        print('Press enter to exit')
        
        input()
        
