#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        
        # Read user input
        command = input('> ')
        
        # Execute command
        if command == 'exit':
            break
        else:
            print(command)
            
    print('Bye!')
<|/ file filename=