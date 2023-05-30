#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    
    if len(sys.argv) != 2:
        sys.exit('Usage: %s <words>' % sys.argv[0])
    
    words = sys.argv[1].split()
    
    words = [word for word in words if word]
    
    words = [word.upper() for word in words]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word not in ['