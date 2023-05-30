#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words.sort()
    
    words = [str(word) for word in words]
    
    words = [word.upper() for word in words]
    
    words = [word for word in words if word]
    
    words = [word.lower() for word in words if word]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in 