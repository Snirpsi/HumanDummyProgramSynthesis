#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        exit(1)
    
    words = sys.argv[1:]
    
    words = [w.strip() for w in words]
    
    words = [w.lower() for w in words]
    
    words = [w.upper() for w in words]
    
    words = [w.capitalize() for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.replace('(', '_').replace(')', '_') for w in words]
    
    words = [w.replace(',', '_') for w in words]
    
    words = [w.replace(':', '_') for w in words]
    
    words = [w.replace(';', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace(':', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace(':', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace(':', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace(':', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace(':', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace(':', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace(':', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in 