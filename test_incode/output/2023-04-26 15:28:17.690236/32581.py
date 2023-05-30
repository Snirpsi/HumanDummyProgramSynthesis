#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port and returns numbers. """    
    import sys
    import getopt
    
    try:
        opts, args = getopt.getopt(sys.argv[1:],"h")
    except getopt.GetoptError:
        print("usage: enumerate.py [-h] [-p] [-o] [-a] [-