#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1].split()
    
    words = [w for w in words if w != '']
    
    words = [w for w in words if w.isalpha()]
    
    words = [w for w in words if len(w) > 1]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w.isalnum()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isalpha()]
    
    words = [w for w in words if not w.