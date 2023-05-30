#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of words and removes numbers. """    
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line:
            words.append(line)
            
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word not in 