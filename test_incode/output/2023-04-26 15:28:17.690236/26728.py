#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and returns a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word not in '-/']
    
    words = [word for word in words if word not in '!?']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '`']
    
    words = [word for word in words if word not in '#']
    
    words = [word for word in words if word not in '$%&*()_+{}[]|;:,.<>/?']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    
    words = [word for word in words if word not in '']
    