#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        try:
            command = input('> ')
        except EOFError:
            break
        else:
            command = command.strip()
            if command == 'quit':
                break
            else:
                print('Invalid command: %s' % command)
    
    
<|/ file filename=