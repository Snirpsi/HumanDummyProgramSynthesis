#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or adds a list of words. """    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    if len(words) == 0:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = words.split(',')
    
    words = [w.strip() for w in words]
    
    words = [w.lower() for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace('_', ' ') for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_'