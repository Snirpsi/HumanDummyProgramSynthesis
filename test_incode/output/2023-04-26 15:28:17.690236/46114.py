#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or stores words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    words = [word for word in words if word]
    
    words = [word.lower() for word in words]
    
    words = [word.upper() for word in words]
    
    words = [word.capitalize() for word in words]
    
    words = [word.title() for word in words]
    
    words = [word.swapcase() for word in words]
    
    words = [word.swapcase() for word in words if word]
    
    words = [word.swapcase() for word in words if word.isalpha()]
    
    words = [word.swapcase() for word in words if word.isdigit()]
    
    words = [word.swapcase() for word in words if word.islower()]
    
    words = [word.swapcase() for word in words if word.isupper()]
    
    words = [word.swapcase() for word in words if word.isalnum()]
    
    words = [word.swapcase() for word in words if word.isspace()]
    
    words = [word.swapcase() for word in words if word.isalnum()]
    
    words = [word.swapcase() for word in words if word.isdigit()]
    
    words = [word.swapcase() for word in words if word.isalpha()]
    
    words = [word.swapcase() for word in words if word.isalnum()]
    
    words = [word.swapcase() for word in words if word.isspace()]
    
    words = [word.swapcase() for word in words if word.isalnum()]
    
    words = [word.swapcase() for word in words if word.isdigit()]
    
    words = [word.swapcase() for word in words if word.isalpha()]
    
    words = [word.swapcase() for word in words if word.isalnum()]
    
    words = [word.swapcase() for word in words if word.isspace()]
    
    words = [word.swapcase() for word in words if word.isalnum()]
    
    words = [word.swapcase() for word in words if word.isdigit()]
    
    words = [word.swapcase() for word in words if word.isalpha()]
    
    words = [word.swapcase() for word in words if word.isalnum()]
    
    words = [word.swapcase() for word in words if word.isspace()]
    
    words = [word.swapcase() for word in words if word.isalnum()]