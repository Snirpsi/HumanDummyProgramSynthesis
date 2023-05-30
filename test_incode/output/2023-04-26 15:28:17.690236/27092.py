#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and converts numbers. """    
    
    import sys
    
    words = [w.strip() for w in sys.stdin.readlines()]
    numbers = [int(n) for n in sys.stdin.readlines()]
    
    words = [w.lower() for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.capitalize() for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.title() for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace(' ', '_') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace('_', ' ') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace(',', '') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace(':', '') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace(';', '') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace('!', '') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace('?', '.') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace(':', '') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace(';', '') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace('!', '') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace('?', '.') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace(':', '') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace(';', '') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace('!', '') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace('?', '.') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace(':', '') for w in words]
    numbers = [int(n) for n in numbers]
    
    words = [w.replace(';', '') for w in word