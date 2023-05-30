#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words. """    
    import sys
    words = sys.argv[1:]
    words = [word.lower() for word in words]
    words = [word for word in words if word.isalpha()]
    words = [word for word in words if word not in '