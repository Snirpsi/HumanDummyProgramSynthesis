#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input or stores a port. """    
    
    port = int(input('Enter a port number: '))
    
    while True:
        print('You entered a port', port)
        
        choice = input('Do you want to remove it? y/n')
        
        if choice == 'y':
            print('Removing port', port)
            
            