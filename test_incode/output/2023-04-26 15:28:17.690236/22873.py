#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or iterates over a list of numbers. """    
    import sys
    import getopt
    
    ports = []
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        sys.exit(2)
    
    for o, a in opts:
        if o == '-h':
            print('Enumerates all ports or iterates over a list of numbers')
            sys.exit()
        elif o == '-a':
            ports = [int(x) for x in a]
        else:
            assert False, "unhandled option"
    
    for port in ports:
        print(port)
    
