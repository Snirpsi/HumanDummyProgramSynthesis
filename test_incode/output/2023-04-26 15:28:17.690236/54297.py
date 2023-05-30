#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    words = [line.strip() for line in sys.stdin.readlines()]
    
    removed = [word for word in words if word not in words]
    
    sys.stdout.writelines(removed)
    
    