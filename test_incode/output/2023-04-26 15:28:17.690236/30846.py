#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words and converts a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        exit(1)
    
    words = sys.argv[1:]
    
    words = words.split()
    
    words = list(set(words))
    
    words.sort()
    
    port = int(sys.argv[1])
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [