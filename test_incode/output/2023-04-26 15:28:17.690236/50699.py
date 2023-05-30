#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    from getopt import getopt, GetoptError
    
    try:
        opts, args = getopt(sys.argv[1:], 'h', ['help'])
    except GetoptError as err:
        print(str(err))
        sys.exit(2)
    
    numbers = []
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('Usage: python webserver.py [-h] [-p PORT]')
            sys.exit()
        elif opt in ('-p', '--port'):
            port = int(arg)
        else:
            numbers.append(arg)
    
    if len(numbers) == 0:
        print('Usage: python webserver.py [-h] [-p PORT]')
        sys.exit()
    
    web