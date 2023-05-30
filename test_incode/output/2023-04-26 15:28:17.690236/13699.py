#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words or removes all ports. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <file> [<file>]" % sys.argv[0])
        sys.exit()
    
    file = sys.argv[1]
    
    words = []
    
    for line in open(file, 'r'):
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        words = words + line.split()
    
    words = [word for word in words if len(word) > 0]
    
    words = [word for word in words if word != '']
    
    words = [word for word in words if word != '#']
    
    words = [word for word in words if word != '!']
    
    words = [word for word in words if word != '?']
    
    words = [word for word in words if word != '!']
    
    words = [word for word in words if word != '?']
    
    words = [word for word in words if word != '!']
    
    words = [word for word in words if word != '?']
    
    words = [word for word in words if word != '!']
    
    words = [word for word in words if word != '?']
    
    words = [word for word in words if word != '!']
    
    words = [word for word in words if word != '?']
    
    words = [word for word in words if word != '!']
    
    words = [word for word in words if word != '?']
    
    words = [word for word in words if word != '!']
    
    words = [word for word in words if word != '?']
    
    words = [word for word in words if word != '!']
    
    words = [word for word in words if word != '?']
    
    words = [word for word in words if word != '!']
    
    words = [word for word in words if word != '?']
    
    words = [word for word in words if word != '!']
    
    words = [word for word in words if word != '?']
    
    words = [word for word in words if word != '!']
    
    words = [word for word in words if word != '?']
    
    words = [word for word in words if word != '!']
    
    words = [word for word in words if word != '?']
    
    words = [word for word in words if word != '!']
    
    words = [word for word in words if word != '?']
    
    words = [word for word in 