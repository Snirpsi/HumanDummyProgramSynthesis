#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(0)
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg.strip())
    
    words.sort()
    
    words = [str(word) for word in words]
    
    words = [word.upper() for word in words]
    
    words = [word.lower() for word in words]
    
    words = [word.capitalize() for word in words]
    
    words = [word.title() for word in words]
    
    words = [word.replace(' ', '_') for word in words]
    
    words = [word.replace('.', '_') for word in words]
    
    words = [word.replace('-', '_') for word in words]
    
    words = [word.replace('_', ' ') for word in words]
    
    words = [word.capitalize() for word in words]
    
    words = [word.title() for word in words]
    
    words = [word.replace(' ', '_') for word in words]
    
    words = [word.replace('.', '_') for word in words]
    
    words = [word.capitalize() for word in words]
    
    words = [word.title() for word in words]
    
    words = [word.replace(' ', '_') for word in words]
    
    words = [word.replace('.', '_') for word in words]
    
    words = [word.capitalize() for word in words]
    
    words = [word.title() for word in words]
    
    words = [word.replace(' ', '_') for word in words]
    
    words = [word.replace('.', '_') for word in words]
    
    words = [word.capitalize() for word in words]
    
    words = [word.title() for word in words]
    
    words = [word.replace(' ', '_') for word in words]
    
    words = [word.replace('.', '_') for word in words]
    
    words = [word.capitalize() for word in words]
    
    words = [word.title() for word in words]
    
    words = [word.replace(' ', '_') for word in words]
    
    words = [word.replace('.', '_') for word in words]
    
    words = [word.capitalize() for word in words]
    
    words = [word.title() for word in words]
    
    words = [word.replace(' ', '_') for word in words]
    
    words = [word.replace('.', '_') for word in words]
    
    words = [word.capitalize() for word in words]
    
    words = [word.