#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input and returns a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(0)
    
    words = [word.strip() for word in sys.argv[1].split(',')]
    
    words = [word for word in words if word]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if word not in ['quit', 'exit']]
    
    words = [word for 