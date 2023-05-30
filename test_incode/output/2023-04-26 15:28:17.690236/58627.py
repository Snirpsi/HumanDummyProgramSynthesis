#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input or returns user input. """    
    while True:
        command = input('> ')
        if command == 'exit':
            break
        else:
            print(command)
            
