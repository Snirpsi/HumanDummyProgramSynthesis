#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [w.lower() for w in words]
    
    words = [w for w in words if w.isalpha()]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w.isspace()]
    
    words = [w for w in words if not w in '-']
    
    words = [w for w in words if not w in '!@#$%^&*()_+{}[]:;"\'<>,.?/']
    
    words = [w for w in words if not w in '`~']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '(){}']
    
    words = [w for w in words if not w in '<>']
    
    words = [w for w in words if not w in '[]']
    
    words = [w for w in words if not w in '<>{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]{}']
    
    words = [w for w in words if not w in '[]