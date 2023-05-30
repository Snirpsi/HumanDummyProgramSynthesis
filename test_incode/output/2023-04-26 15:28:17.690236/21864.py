#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in 