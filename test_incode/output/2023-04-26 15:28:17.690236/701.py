#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or prints numbers. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [word|number]" % sys.argv[0])
        sys.exit()
    
    command = sys.argv[1]
    
    if command == 'word':
        word()
    elif command == 'number':
        number()
    else:
        print("Unknown command: %s" % command)
        sys.exit()
    
