#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and stores user input. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    words.sort()
    
    words = [w.upper() for w in words]
    
    words = [w.capitalize() for w in words]
    
    words = [w.title() for w in words]
    
    words = [w.replace(' ', '_') for w in words]
    
    words = [w.replace('(', '_') for w in words]
    
    words = [w.replace(')', '_') for w in words]
    
    words = [w.replace(',', '_') for w in words]
    
    words = [w.replace(':', '_') for w in words]
    
    words = [w.replace(';', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('\'', '_') for w in words]
    
    words = [w.replace('\"', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('\'', '_') for w in words]
    
    words = [w.replace('\"', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('\'', '_') for w in words]
    
    words = [w.replace('\"', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('\'', '_') for w in words]
    
    words = [w.replace('\"', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('\'', '_') for w in words]
    
    words = [w.replace('\"', '_') for w in words]
    
    words = [w.replace('!', '_') for w in words]
    
    words = [w.replace('?', '_') for w in words]
    
    words = [w.replace('\'', '_') for 