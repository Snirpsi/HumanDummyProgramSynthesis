#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input and iterates over fruits. """    
    
    import sys
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fruits', help='list of fruits', nargs='+')
    args = parser.parse_args()
    
    for fruit in args.fruits:
        print('{} is {}