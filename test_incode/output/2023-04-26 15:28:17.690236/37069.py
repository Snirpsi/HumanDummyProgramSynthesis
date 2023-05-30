#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or removes a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        lines = f.readlines()
    
    numbers = []
    words = []
    
    for line in lines:
        line = line.strip()
        
        if line.startswith("#"):
            continue
        
        numbers.append(int(line))
        words.append(line)
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(map(lambda x: x * 2, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
