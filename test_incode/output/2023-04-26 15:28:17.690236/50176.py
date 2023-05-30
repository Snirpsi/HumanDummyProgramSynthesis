#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words and removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        exit(1)
    
    words = sys.argv[1:]
    
    words = [w.strip() for w in words]
    
    words = [w for w in words if len(w) > 0]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if len(w) > 0]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w 