#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports. """    
    import sys
    import getopt
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], '', ['help'])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('Usage: %s [-h] [-p] [-d] [-t] [-a] [-