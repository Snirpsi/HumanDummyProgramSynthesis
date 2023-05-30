#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or iterates over user input. """    
    
    import sys
    
    # Parse command line arguments
    args = sys.argv[1:]
    
    # Enumerate fruits and print results
    if args.fruit:
        fruit = Fruit()
        fruit.enumerate()
        
    # Iterate over user input and print results
    elif args.input:
        fruit = Fruit()
        fruit.iterate(args.input)
    
    # Print usage and exit
    else:
        print('Usage: %s [-f fruit] [-i input] [-h] [-p port] [-v] [-d dir]' % sys.argv[0])
        print('       %s [-f fruit] [-i input] [-h] [-p port] [-v] [-d dir]' % sys.argv[0])
        print('       %s [-f fruit] [-i input] [-h] [-p port] [-v] [-d dir]' % sys.argv[0])
        print('       %s [-f fruit] [-i input] [-h] [-p port] [-v] [-d dir]' % sys.argv[0])
        print('       %s [-f fruit] [-i input] [-h] [-p port] [-v] [-d dir]' % sys.argv[0])
        print('       %s [-f fruit] [-i input] [-h] [-p port] [-v] [-d dir]' % sys.argv[0])
        print('       %s [-f fruit] [-i input] [-h] [-p port] [-v] [-d dir]' % sys.argv[0])
        print('       %s [-f fruit] [-i input] [-h] [-p port] [-v] [-d dir]' % sys.argv[0])
        print('       %s [-f fruit] [-i input] [-h] [-p port] [-v] [-d dir]' % sys.argv[0])
        print('       %s [-f fruit] [-i input] [-h] [-p port] [-v] [-d dir]' % sys.argv[0])
        print('       %s [-f fruit] [-i input] [-h] [-p port] [-v] [-d dir]' % sys.argv[0])
        print('       %s [-f fruit] [-i input] [-h] [-p port] [-v] [-d dir]' % sys.argv[0])
        print('       %s [-f fruit] [-i input] [-h] [-p port] [-v] [-d dir]' % sys.argv[0])
        print('       %s [-f fruit] [-i input] [-h] [-p port] [-v] [-d dir]' % sys.argv[0])
        print('       %s [-f fruit] [-i input] [-h] [-p port] [-v] [-