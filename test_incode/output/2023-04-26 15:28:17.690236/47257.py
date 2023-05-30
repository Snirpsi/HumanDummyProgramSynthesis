#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words or stores all ports. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: python multiply_word.py <words>")
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    words = [word for word in words if word]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word not in [' ', '\n', '\t']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in words if word not in ['.', '!', '?']]
    
    words = [word for word in word