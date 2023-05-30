#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        command = input('> ')
        if command == 'exit':
            break
        
        command = command.split()
        
        if command[0] == 'remove':
            command[1] = int(command[1])
            
            command[2] = command[2]