#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports and converts a list of words. """    
    ports = list('abcdefghijklmnopqrstuvwxyz')
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        for port in ports:
            print('Port:', port)
            for word in words:
                print('Word:', word)
                
        print('Press the enter key to exit')
        
        try:
            line = input('> ')
        except EOFError:
            print('Goodbye!')
            break
        
        if line == '':
            break
        else:
            print('Invalid input')
        
