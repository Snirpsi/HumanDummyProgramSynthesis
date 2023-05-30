#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or prints a port. """    
    while True:
        try:
            port = input('Enter a port number: ')
            break
        except KeyboardInterrupt:
            print('\nExiting...')
            sys.exit(0)
        except EOFError:
            print('\nExiting...')
            sys.exit(0)
        
    print('\nConverting port to 