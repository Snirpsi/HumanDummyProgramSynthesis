#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words or adds a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [w.strip() for w in words]
    
    words = [w.lower() for w in words]
    
    words = [w.upper() for w in words]
    
    words = [w.capitalize() for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.replace('(', '_') for w in words]
    
    words = [w.replace(')', '_') for w in words]
    
    words = [w.replace(',', '_') for w in words]
    
    words = [w.replace(':', '_') for w in words]
    
    words = [w.replace(';', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
