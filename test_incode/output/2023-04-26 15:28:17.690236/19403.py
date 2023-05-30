#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and converts fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    with open('fruits.txt') as file:
        for line in file:
            line = line.strip()
            
            if line:
                words.append(line)
    
    words.sort()
    
    words = [word for word in words if word.isalpha()]
    
    words = [word.upper() for word in words]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in words]
    
    words = [word for word in words if word not in 