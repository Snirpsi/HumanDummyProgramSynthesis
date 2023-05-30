#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    import os
    
    port = int(sys.argv[1])
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words.sort()
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if word not in ['.', '?', '!', ':', ';', '[', ']', '{', '}', '(', ')', '[', ']', '{', '}']]
    
    words = [word for word in words if word not in ['.', '?', '!', ':', ';', '[', ']', '{', '}', '(', ')', '[', ']', '{', '}']]
    
    words = [word for word in words if word not in ['.', '?', '!', ':', ';', '[', ']', '{', '}', '(', ')', '[', ']', '{', '}']]
    
    words = [word for word in words if word not in ['.', '?', '!', ':', ';', '[', ']', '{', '}', '(', ')', '[', ']', '{', '}']]
    
    words = [word for word in words if word not in ['.', '?', '!', ':', ';', '[', ']', '{', '}', '(', ')', '[', ']', '{', '}']]
    
    words = [word for word in words if word not in ['.', '?', '!', ':', ';', '[', ']', '{', '}', '(', ')', '[', ']', '{', '}']]
    
    words = [word for word in words if word not in ['.', '?', '!', ':', ';', '[', ']', '{', '}', '(', ')', '[', ']', '{', '}']]
    
    words = [word for word in words if word not in ['.', '?', '!', ':', ';', '[', ']', '{', '}', '(', ')', '[', ']', '{', '}']]
    
    words = [word for word in words if word not in ['.', '?', '!', ':', ';', '[', ']', '{', '}', '(', ')', '[', ']', '{', '}']]
    
    words = [word for word in 