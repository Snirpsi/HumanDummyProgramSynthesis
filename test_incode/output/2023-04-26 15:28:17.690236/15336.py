#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s word" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1].split()
    
    words = [w for w in words if w]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isupper()]
    
    words = [w for w in words if not w.islower()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isupper()]
    
    words = [w for w in words if not w.islower()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isupper()]
    
    words = [w for w in words if not w.islower()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isupper()]
    
    words = [w for w in words if not w.islower()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not 