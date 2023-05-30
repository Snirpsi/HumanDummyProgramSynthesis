#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or enumerates a port. """    
    while True:
        port = input('Enter a port number: ')
        if port == 'exit':
            break
        elif port == 'help':
            print('''
            Enter a port number: 
            ''')
        else:
            