#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    words = [x.strip() for x in sys.stdin.read().split(' ')]
    
    words = [w for w in words if w]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isupper()]
    
    words = [w for w in words if not w.islower()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isupper()]
    
    words = [w for w in words if not w.islower()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isupper()]
    
    words = [w for w in words if not w.islower()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isupper()]
    
    words = [w for w in words if not w.islower()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in word