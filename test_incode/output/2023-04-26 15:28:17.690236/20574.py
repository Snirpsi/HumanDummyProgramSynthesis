#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers. """    
    import sys
    while True:
        sys.stdout.write("%d\n" % i)
        sys.stdout.flush()
        i = i + 1
        if i > sys.max