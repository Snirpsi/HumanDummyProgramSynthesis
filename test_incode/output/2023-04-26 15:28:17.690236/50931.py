#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words and removes numbers. """    
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
        
    words = [word.lower() for word in words]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word not in [' ', '\n', '\t']]
    
    words = [word for word in words if word not in ['.', '?', '!']]
    
    words = [word for word in words if word not in ['\'', '\"', '\'\'', '"\'', '"\'\'']]
    
    words = [word for word in words if word not in ['\'\'', '"\'\'']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for 